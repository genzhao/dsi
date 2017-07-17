import scrapy
from nikescrape.items import JimmyjazzscrapeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs

class JimmyjazzscrapeSpider(CrawlSpider):

	name = 'JimmyjazzCrawl'
#	handle_httpstatus_all = True
	start_urls = ['http://www.jimmyjazz.com/featured-brand/jordan/listing?category=footwear',
				  'https://www.stadiumgoods.com/nike',
				  'https://www.stadiumgoods.com/adidas']

	#Defining rule to crawl next pages

	rules = (Rule(LinkExtractor(restrict_xpaths = ['//*[@id="container"]/div[1]/div/div[1]/div[2]/div/div[4]/div/div/a']),follow=True,callback='parse_data'),
			 Rule(LinkExtractor(restrict_xpaths = ['//*[@id="container"]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/a']),follow=True,callback='parse_data'),)


	def parse_data(self,response):
		sku = response.xpath('//*[@id="container"]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/span[2]/text()').extract()
		brand_name = response.xpath('//*[@id="container"]/div[1]/div/div[1]/div[2]/div[1]/div[2]/h1/span[1]/text()').extract()
		shoe_name = response.xpath('//*[@id="container"]/div[1]/div/div[1]/div[2]/div[1]/div[2]/h1/span[2]/text()').extract()
		colorway = response.xpath('//*[@id="container"]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]/text()').extract()
		angledfront = response.xpath('//*[@id="container"]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/img[2]/@data-large-img').extract()
		bottomview = response.xpath('//*[@id="container"]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/img[4]/@data-large-img').extract()
		frontback2shoe = response.xpath('//*[@id="container"]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/img[8]/@data-large-img').extract()


		for sku_code, brand, shoe, color, front, bottom, frontback in zip(sku, brand_name, shoe_name, colorway, angledfront, bottomview, frontback2shoe):
			item = JimmyjazzscrapeItem()
			item['sku'] = sku_code
			item['brand_name'] = brand
			item['shoe_name'] = shoe
			item['colorway'] = color
			item['angledfront'] = front
			item['bottomview'] = bottom
			item['frontback2shoe'] = frontback

			yield item
