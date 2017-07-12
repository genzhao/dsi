import scrapy
from nikescrape.items import JourneyscrapeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs

class JourneyscrapeSpider(CrawlSpider):

	name = 'JourneyCrawl'
#	handle_httpstatus_all = True
	start_urls = ['https://www.journeys.com/products/sneakers?g=m']

	#Defining rule to crawl next pages

	rules = (Rule(LinkExtractor(restrict_xpaths = ['//*[@id="listingProducts"]/div/a']),follow=True,callback='parse_data'),
			 Rule(LinkExtractor(restrict_xpaths = ['//*[@id="pageContent"]/div/div[2]/div[1]/div[2]/ul/li/a']),follow=True,callback='parse_data'),)


	def parse_data(self,response):
		shoe_link = response.xpath('//*[@id="listingProducts"]/div/a/@href').extract()
		brand_name = response.xpath('//*[@id="detailWide"]/li[1]/a/text()').extract()
		shoe_name = response.xpath('//*[@id="detailProdName"]/text()').extract()
		colorway = response.xpath('//*[@id="headerInfo"]/div[1]/text()').extract()
		bottomview = response.xpath('//*[@id="detailAltViews"]/ul/li[6]/a/@href').extract()
		angledfront = response.xpath('//*[@id="detailAltViews"]/ul/li[1]/a/@href').extract()
		angledheel = response.xpath('//*[@id="detailAltViews"]/ul/li[3]/a/@href').extract()
		medialfrontright = response.xpath('//*[@id="detailAltViews"]/ul/li[2]/a/@href').extract()
		toeview = response.xpath('//*[@id="detailAltViews"]/ul/li[5]/a/@href').extract()

		for brand, shoe, bottom, front, heel, medial, toe in zip(brand_name, shoe_name, bottomview, angledfront, angledheel, medialfrontright, toeview):
			item = JourneyscrapeItem()
			abs_url = response.urljoin(shoe_link)
			item['shoe_link'] = abs_url
			item['brand_name'] = brand.split(' ')[1]
			item['shoe_name'] = shoe
			item['bottomview'] = bottom
			item['angledfront'] = front
			item['angledheel'] = heel
			item['medialfrontright'] = medial
			item['toeview'] = toe
			item['colorway'] = str(colorway[1]).strip()

			yield item
