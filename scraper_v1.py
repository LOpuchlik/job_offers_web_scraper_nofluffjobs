
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

options = webdriver.ChromeOptions()
# specifying the chrome beta location
options.binary_location = '/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta'
#CHROMEDRIVER_PATH_103 = Service("/Users/jagoodka/Dropbox/Jagoda/Projekty/pracujWebscraper/chromedriver")
# path for chromewebdriver v. 104
CHROMEDRIVER_PATH_104_beta = Service("/Users/jagoodka/Desktop/chromedriver")

def get_jobs(num_jobs, slp_time):

    driver = webdriver.Chrome(service=CHROMEDRIVER_PATH_104_beta, options=options)
    driver.set_window_size(1120, 1000)
    driver.implicitly_wait(5)

    #keyword=""


    url="https://nofluffjobs.com/pl/?gclid=CjwKCAjwt7SWBhAnEiwAx8ZLalFn7q9GmI1YOjJrr-_whP-yLQGBHs8nfXb_lajjmo-lhfyo9DoDYhoC-jwQAvD_BwE&criteria=keyword%3Ddata,analyst&page=1"
    driver.get(url)

    jobs = []
    #Test for the "Cookies" prompt and get rid of it.
    try:
        btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="onetrust-accept-btn-handler"]')))
        btn.click()
    except ElementClickInterceptedException:
        pass

    while len(jobs) < num_jobs:
        time.sleep(10)

        #Going through each job in this page
        job_postings=driver.find_elements(By.XPATH, '//a[contains(@class,"posting-list-item")]')


        # getting links to all separate job offers on the page stored in posting_refs
        job_postings_refs = []
        for job_posting in job_postings:
            job_postings_refs.append(job_posting.get_attribute('href'))

        for job_posting_ref in job_postings_refs:
            if len(jobs) != 0:
                print("Already scraped: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                print("Done!")
                break 
            collected_successfully = False
            time.sleep(.5)
            driver.get(job_posting_ref)  #You might 
            time.sleep(.5)

            while not collected_successfully:

                try:
                    company_name = driver.find_element(By.XPATH, '//*[@id="postingCompanyUrl"]').get_property('text')
                    location = driver.find_element(By.XPATH, '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/common-main-loader/section/div[2]/div[2]/common-apply-box/div[1]/div[2]/div/ul').text
                    job_title = driver.find_element(By.XPATH, '//*[@id="posting-header"]/div/div/h1').text
                    salary_estimate = driver.find_element(By.XPATH, '//*[@class="mb-0"]').text
                    contract_type = driver.find_element(By.XPATH, '//*[@class="paragraph font-size-14 d-flex align-items-center flex-wrap type position-relative"]').text
                    jobs.append({
                    "Job Title" : job_title,
                    "Salary Estimate" : salary_estimate,
                    "Company Name" : company_name,
                    "Contract type" : contract_type,
                    "Location" : location
                    })
                    collected_successfully = True
                except NoSuchElementException:
                    company_name = -1
                    location = -1
                    job_title = -1
                    salary_estimate = -1
                    contract_type = -1
                    print("Exception")
                    time.sleep(.5)

  #Clicking on the "next page" button
        # try:
        #     url = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-postings-search/div/common-main-loader/div/nfj-search-results/div/nfj-pagination/ul/li[5]/a'))).get_attribute('href')
        #     driver.get(url)
        #     print("Clicked for next page")
        #     WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.XPATH, '/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-postings-search/div/common-main-loader/div/nfj-search-results/div/nfj-pagination/ul/li[5]/a')))
        # except TimeoutException:
        #     print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
        #     break

   

    return pd.DataFrame(jobs)

