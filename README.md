# job_offers_web_scraper_nofluffjobs
Script allowing for webscraping job postings from NoFLuffJobs portal

The script is written using Selenium Webdriver.
Library requirements are stored in requirements.txt file
The user has to specify their path to the chromedriver executable file.

The script allows to scrape specified number of job postings by searched by a specified keyword(s).

The collected data is saved as a .csv file.

### TODO
##### Scraping
- add more features to be scraped (e.g. required skills, job description etc.)
- scrape more data (every couple of days) when new job postings show up
- at the end, merge all .csv files together
##### Cleaning
- remove duplicates (rows)
- remove white spaces and other unnecessary characters
- check data formats; change to numerical when necessary
- do simple feature engineering e.g. make column - average salary from the salary range
##### Analysis
- visualise the collected data
- evaluate basic statistics
##### Modelling
- predict salary value that one should state during job interview
