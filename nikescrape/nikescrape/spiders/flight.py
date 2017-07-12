import scrapy
from nikescrape.items import FlightscrapeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs

class FlightscrapeSpider(CrawlSpider):

	name = 'FlightCrawl'
#	handle_httpstatus_all = True
	start_urls = ['https://www.flightclub.com/air-jordans?id=34&limit=90','https://www.flightclub.com/nike?id=62&limit=90','https://www.flightclub.com/adidas?id=18&limit=90','https://www.flightclub.com/footwear?id=17&limit=90']

	#Defining rule to crawl next pages

	rules = (Rule(LinkExtractor(restrict_xpaths = ['//*[@id="entire-page-wrap"]/div/div/div/div/ul/li/a']),follow=True,callback='parse_data'),
			 Rule(LinkExtractor(restrict_xpaths = ['//*[@id="toolbar-header"]/div[1]/a']),follow=True,callback='parse_data'),)


	def parse_data(self,response):
		brand_name = response.xpath('//*[@id="entire-page-wrap"]/div[4]/div[2]/div/div[2]/div[2]/div[1]/h2/text()').extract()
		shoe_name = response.xpath('//*[@id="entire-page-wrap"]/div[4]/div[2]/div/div[2]/div[2]/div[1]/h1/text()').extract()
		colorway = response.xpath('//*[@id="entire-page-wrap"]/div[4]/div[2]/div/div[2]/div[2]/div[3]/div/ul/li[2]/text()').extract()
		lateralfrontright = response.xpath('//*[@id="entire-page-wrap"]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/ul/li/a/@data-url-zoom').extract()
#		bottomview = response.xpath('//*[@id="entire-page-wrap"]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/ul/li/a/@data-url-zoom').extract()
#		angledfront = response.xpath('//*[@id="entire-page-wrap"]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/ul/li/a/@data-url-zoom').extract()
#		angledheel = response.xpath('//*[@id="entire-page-wrap"]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/ul/li/a/@data-url-zoom').extract()

		for brand, shoe, color in zip(brand_name, shoe_name, colorway):
			item = FlightscrapeItem()
			item['brand_name'] = brand
			item['shoe_name'] = shoe
			item['colorway'] = color
			item['lateralfrontright'] = lateralfrontright[0]
			item['bottomview'] = lateralfrontright[1]
			item['angledfront'] = lateralfrontright[2]
			item['angledheel'] = lateralfrontright[3]

			yield item
