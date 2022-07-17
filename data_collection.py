#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:32:33 2022

@author: jagoodka
"""

import scraper_v1 as sc 
import pandas as pd 

# give the location of your chromedriver executable file
path = "/Users/jagoodka/Dropbox/Jagoda/Projekty/pracujWebscraper/chromedriver"

df = sc.get_jobs(num_jobs=10, slp_time=2)

df.to_csv('sample_of_scraped_data.csv', index = False)
