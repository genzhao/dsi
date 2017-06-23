import scrapy
from craigslist.items import CraigslistItem
from bs4 import BeautifulSoup as bs


class clBaseSpider(scrapy.Spider):
	name = "clBase"
	start_urls = ['https://sfbay.craigslist.org/search/rva']

	def parse(self,response):
		#/'//span[@class="company"]/span'
		#//h2/a/@title'
		prices = response.xpath('//span[@class="result-price"]/text()').extract()
		links = response.xpath('//p/a/@href').extract()
		listings = response.xpath('//p/a[@class="result-title hdrlnk"]/text()').extract()

		for price,link,listing in zip(prices,links,listings):
			item = CraigslistItem()
			item['price'] = price
			item['link'] = "https://sfbay.craigslist.org" + str(link)
			item['listing'] = listing
			yield item
