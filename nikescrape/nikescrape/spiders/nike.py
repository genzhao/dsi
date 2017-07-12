import scrapy
from nikescrape.items import NikescrapeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs

class NikescrapeSpider(CrawlSpider):

	name = 'NikeCrawl'

	start_urls = ['https://store.nike.com/us/en_us/pw/mens-shoes/7puZoi3?ipp=120']

	#Defining rule to crawl next pages

	rules = (Rule(LinkExtractor(restrict_xpaths = ['//div[@data-pdpurl]']),follow=True,callback='parse_data'),
			 Rule(LinkExtractor(restrict_xpaths = ['//*[@id="content"]/div[2]/div[1]/div[2]/div[3]/div/ul/li/a']),follow=True,callback='parse_data'),)

	def parse_data(self,response):
		shoe_name = response.xpath('//div/h1/text()').extract()
		colorway = response.xpath('//span[@class="colorText"]/text()').extract()
		img_links = response.xpath('//div[2]/ul/li/img[@class="exp-pdp-alt-image"]/@data-large-image').extract()

		for shoe, color, img_link in zip(shoe_name,colorway, img_links):
			item = NikescrapeItem()
			item['shoe_name'] = shoe
			item['colorway'] = color
			item['img_a'] = img_links[0]
			item['img_b'] = img_links[1]
			item['img_c'] = img_links[2]
			item['img_d'] = img_links[3]
			item['img_e'] = img_links[4]
			item['img_f'] = img_links[5]
			yield item
