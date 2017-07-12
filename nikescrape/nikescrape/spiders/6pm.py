import scrapy
from nikescrape.items import SixscrapeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs

class SixscrapeSpider(CrawlSpider):

	name = 'SixCrawl'
#	handle_httpstatus_all = True
	start_urls = ['http://www.6pm.com/sneakers-athletic-shoes/CK_XARC81wHiAgIBAg.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/']

	#Defining rule to crawl next pages

	rules = (Rule(LinkExtractor(restrict_xpaths = ['//*[@id="searchResults"]/a']),follow=True,callback='parse_data'),
			 Rule(LinkExtractor(restrict_xpaths = ['//*[@id="resultWrap"]/div[1]/div[2]/a']),follow=True,callback='parse_data'),)


	def parse_data(self,response):
		shoe_link = response.xpath('//*[@id="searchResults"]/a/@href').extract()
		brand_name = response.xpath('//*[@id="productStage"]/h1/a[1]/text()').extract()
		shoe_name = response.xpath('//*[@id="productStage"]/h1/a/@content').extract()
		colorcode = response.xpath('//*[@id="color"]/option/@value').extract()
		colorway2 = response.xpath('//*[@id="colors"]/p/text()').extract()
		colorway = response.xpath('//*[@id="color"]/option/text()').extract()
		topview = response.xpath('//*[@id="frontrow-1"]/@href').extract()
		bottomview = response.xpath('//*[@id="frontrow-2"]/@href').extract()
		lateralfrontleft = response.xpath('//*[@id="frontrow-3"]/@href').extract()
		heelview = response.xpath('//*[@id="frontrow-4"]/@href').extract()
		medialfrontright = response.xpath('//*[@id="frontrow-5"]/@href').extract()
		toeview = response.xpath('//*[@id="frontrow-6"]/@href').extract()

		for brand, shoe, top, bottom, lateral, heel, medial, toe in zip(brand_name, shoe_name, topview, bottomview, lateralfrontleft, heelview, medialfrontright, toeview):
			item = SixscrapeItem()
			abs_url = response.urljoin(shoe_link)
			item['shoe_link'] = abs_url
			item['brand_name'] = brand
			item['shoe_name'] = shoe
			item['topview'] = top
			item['bottomview'] = bottom
			item['lateralfrontleft'] = lateral
			item['heelview'] = heel
			item['medialfrontright'] = medial
			item['toeview'] = toe
			item['colorway'] = colorway2
			item['colorcode'] = abs_url.rsplit('color/')[-1]
			temp_dict = zip((code for code in colorcode), (color for color in colorway))
			for key, value in temp_dict:
				if key in item['colorcode']:
					item['colorway'] = value



			yield item
