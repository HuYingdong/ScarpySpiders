# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    avatar_url = Field()
    gender = Field()
    headline = Field()
    url_token = Field()
    follower_count = Field()




