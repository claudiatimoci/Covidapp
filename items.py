# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html



import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# class ReviewsCovidCases(scrapy.Item):
#      country  = scrapy.Field()
#      deaths    = scrapy.Field()
#      death_rate = scrapy.Field()
#      total_cases   = scrapy.Field()
     


class ReviewsCovidCases(scrapy.Item):
    # Your item fields here
    country = scrapy.Field()
    deaths = scrapy.Field()
    death_rate = scrapy.Field()
    total_cases = scrapy.Field()
