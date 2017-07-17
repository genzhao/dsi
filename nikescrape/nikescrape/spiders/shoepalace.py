import scrapy
from nikescrape.items import ShoepalacescrapeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs

class ShoepalacescrapeSpider(CrawlSpider):

	name = 'ShoepalaceCrawl'
#	handle_httpstatus_all = True
	start_urls = ['http://www.shoepalace.com/men/footwear/shoes/?limit=all','http://www.shoepalace.com/women/footwear/shoes/?limit=all']

	#Defining rule to crawl next pages

	rules = (Rule(LinkExtractor(restrict_xpaths = ['/html/body/div/div/div/div/div/div/div/div/div/a']),follow=True,callback='parse_data'),)


	def parse_data(self,response):
		brand_name = response.xpath('//*[@id="background"]/div[4]/h1/a/span/text()').extract()
		shoe_name = response.xpath('//*[@id="background"]/div[4]/h2[1]/text()').extract()
		colorway = response.xpath('//*[@id="background"]/div[4]/h2[1]/text()').extract()
		sku = response.xpath('//*[@id="background"]/div[4]/div[5]/@content').extract()
		lateralfrontright = response.xpath('//*[@id="productview"]/div[2]/div[1]/div/img/@src').extract()
		bottomview = response.xpath('//*[@id="productview"]/div[2]/div[3]/div/img/@src').extract()
		angledfront2shoe = response.xpath('//*[@id="productview"]/div[2]/div[4]/div/img/@src').extract()
		angledheel2shoe = response.xpath('//*[@id="productview"]/div[2]/div[6]/div/img/@src').extract()
		medialfrontleft = response.xpath('//*[@id="productview"]/div[2]/div[2]/div/img/@src').extract()
		top2view = response.xpath('//*[@id="productview"]/div[2]/div[5]/div/img/@src').extract()

		for brand, shoe, color, bottom, front, heel, medial, top, lateral in zip(brand_name, shoe_name, colorway, bottomview, angledfront2shoe, angledheel2shoe, medialfrontleft, top2view, lateralfrontright):
			item = ShoepalacescrapeItem()
			item['brand_name'] = brand
			item['colorway'] = str(colorway).split('(')[1]
			item['shoe_name'] = str(shoe).split('(')[0]
			item['sku'] = sku
			item['lateralfrontright'] = lateral
			item['bottomview'] = bottom
			item['angledheel2shoe'] = heel
			item['angledfront2shoe'] = front
			item['medialfrontleft'] = medial
			item['top2view'] = top

			yield item
