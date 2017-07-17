# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NikescrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        shoe_name = scrapy.Field()
        colorway = scrapy.Field()
        img_links = scrapy.Field()
        img_a = scrapy.Field()
        img_b = scrapy.Field()
        img_c = scrapy.Field()
        img_d = scrapy.Field()
        img_e = scrapy.Field()
        img_f = scrapy.Field()

class ZapposcrapeItem(scrapy.Item):
        shoe_link = scrapy.Field()
        brand_name = scrapy.Field()
        shoe_name = scrapy.Field()
        colorcode = scrapy.Field()
        colorway = scrapy.Field()
        topview = scrapy.Field()
        bottomview = scrapy.Field()
        lateralfrontleft = scrapy.Field()
        heelview = scrapy.Field()
        medialfrontright = scrapy.Field()
        toeview = scrapy.Field()
#        colordict = scrapy.Field()

class SixscrapeItem(scrapy.Item):
        shoe_link = scrapy.Field()
        brand_name = scrapy.Field()
        shoe_name = scrapy.Field()
        colorcode = scrapy.Field()
        colorway = scrapy.Field()
        topview = scrapy.Field()
        bottomview = scrapy.Field()
        lateralfrontleft = scrapy.Field()
        heelview = scrapy.Field()
        medialfrontright = scrapy.Field()
        toeview = scrapy.Field()

class SkatescrapeItem(scrapy.Item):
#        shoe_link = scrapy.Field()
#        brand_name = scrapy.Field()
        shoe_name = scrapy.Field()
        colorway = scrapy.Field()
        topview = scrapy.Field()
        bottomview = scrapy.Field()
        lateralfrontleft = scrapy.Field()
        medialfrontright = scrapy.Field()

class FlightscrapeItem(scrapy.Item):
        brand_name = scrapy.Field()
        shoe_name = scrapy.Field()
        colorway = scrapy.Field()
        lateralfrontright = scrapy.Field()
        bottomview = scrapy.Field()
        angledfront = scrapy.Field()
        angledheel = scrapy.Field()

class JourneyscrapeItem(scrapy.Item):
        shoe_link = scrapy.Field()
        brand_name = scrapy.Field()
        shoe_name = scrapy.Field()
        colorway = scrapy.Field()
        bottomview = scrapy.Field()
        angledfront = scrapy.Field()
        angledheel = scrapy.Field()
        medialfrontright = scrapy.Field()
        toeview = scrapy.Field()

class ShoepalacescrapeItem(scrapy.Item):
        brand_name = scrapy.Field()
        shoe_name = scrapy.Field()
        colorway = scrapy.Field()
        sku = scrapy.Field()
        bottomview = scrapy.Field()
        angledfront2shoe = scrapy.Field()
        angledheel2shoe = scrapy.Field()
        medialfrontleft = scrapy.Field()
        top2view = scrapy.Field()
        lateralfrontright = scrapy.Field()

class StadiumgoodscrapeItem(scrapy.Item):
        sku = scrapy.Field()
        brand_name = scrapy.Field()
        shoe_name = scrapy.Field()
        colorway = scrapy.Field()
        angledfront2shoe = scrapy.Field()
        bottomview = scrapy.Field()
        angledheel2shoe = scrapy.Field()
        lateralfrontleft = scrapy.Field()
        angledfront = scrapy.Field()

class JimmyjazzscrapeItem(scrapy.Item):
        sku = scrapy.Field()
        brand_name = scrapy.Field()
        shoe_name = scrapy.Field()
        colorway = scrapy.Field()
        angledfront = scrapy.Field()
        bottomview = scrapy.Field()
        frontback2shoe = scrapy.Field()
