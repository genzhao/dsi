import scrapy
from nikescrape.items import StadiumgoodscrapeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs

class StadiumgoodscrapeSpider(CrawlSpider):

	name = 'StadiumgoodsCrawl'
#	handle_httpstatus_all = True
	start_urls = ['https://www.stadiumgoods.com/air-jordan',
				  'https://www.stadiumgoods.com/nike',
				  'https://www.stadiumgoods.com/adidas']

	#Defining rule to crawl next pages

	rules = (Rule(LinkExtractor(restrict_xpaths = ['//*[@id="top"]/body/div[2]/div[1]/div/div/div/div/div/div/ul/li/a']),follow=True,callback='parse_data'),
			 Rule(LinkExtractor(restrict_xpaths = ['//*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[3]/div/a']),follow=True,callback='parse_data'),)


	def parse_data(self,response):
		sku = response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[1]/td/text()').extract()
		brand_name = response.xpath('//*[@id="product_addtocart_form"]/section/div[1]/div[2]/div[2]/text()').extract()
		shoe_name = response.xpath('//*[@id="product_addtocart_form"]/section/div[1]/div[2]/h1[@itemprop="name"]/text()').extract()
		colorway = response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[3]/td/text()').extract()
		angledfront2shoe = response.xpath('//*[@id="product_addtocart_form"]/section/div[2]/div[5]/img/@src').extract()
		bottomview = response.xpath('//*[@id="product_addtocart_form"]/section/div[2]/div[4]/img/@src').extract()
		lateralfrontleft = response.xpath('//*[@id="product_addtocart_form"]/section/div[2]/div[3]/img/@src').extract()
		angledheel2shoe = response.xpath('//*[@id="product_addtocart_form"]/section/div[2]/div[6]/img/@src').extract()
		angledfront = response.xpath('//*[@id="product_addtocart_form"]/section/div[2]/div[7]/img/@src').extract()

		for sku_code, brand, shoe, color, front2, bottom, lateral, heel2, front in zip(sku, brand_name, shoe_name, colorway, angledfront2shoe, bottomview, lateralfrontleft, angledheel2shoe, angledfront):
			item = StadiumgoodscrapeItem()
			item['sku'] = sku_code
			item['brand_name'] = brand
			item['shoe_name'] = shoe
			item['colorway'] = color
			item['angledfront2shoe'] = front2
			item['bottomview'] = bottom
			item['lateralfrontleft'] = lateral
			item['angledheel2shoe'] = heel2
			item['angledfront'] = front

			yield item
