
import sys
sys.path.append('../')
import scrapy
from items import ReviewsCovidCases
from scrapy import Request
import streamlit as st
import pandas as pd
import os
import sqlalchemy as db
from WebCrawler.pipelines import DataBase
# from ..pipeline import DataBase

class CovidSpider(scrapy.Spider):
    name = "covid"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["https://www.bbc.com/news/world-51235105"]
    data_base = DataBase('Covid')
    data_base.create_table('CovidCases',
                           country = db.String,
                           deaths = db.String,
                           death_rate = db.String,
                           total_cases = db.String,
                           )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_covid_cases)


    def parse_covid_cases(self, response):
        table1 = response.css('tbody')[0]

        for table in table1.css('tr'):
            item = ReviewsCovidCases()
            try: item['country'] = table.css('td::text')[0].get().strip(),
            except: item['country'] = None,
            try: item['deaths'] = table.css('td::text')[1].get().strip(),
            except: item['deaths'] = None,
            try: item['death_rate'] = table.css('td::text')[2].get().strip(),
            except: item['death_rate'] = None,
            try: item['total_cases']= table.css('td::text')[3].get().strip(),
            except: item['total_cases'] = None

            try:
                self.data_base.add_row('CovidCases',
                                       country = str(item['country']),
                                       deaths = str(item['deaths']),
                                       death_rate = str(item['death_rate']),
                                       total_cases = str(item['total_cases']))
            except Exception as e:
                print(f"Error: {e}")
            yield item
