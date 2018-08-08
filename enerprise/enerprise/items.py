# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class JWcropItem(Item):
    # define the fields for your item here like:
    Overseas_Investment_Enterprises = Field()
    Domestic_Investment_name = Field()
    Investment_Country = Field()
