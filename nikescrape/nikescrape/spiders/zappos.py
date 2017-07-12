import scrapy
from nikescrape.items import ZapposcrapeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs

class ZapposcrapeSpider(CrawlSpider):

	name = 'ZapposCrawl'
#	handle_httpstatus_all = True
	start_urls = ['http://www.zappos.com/sneakers-athletic-shoes/CK_XARC81wHiAgIBAg.zso?s=goliveRecentSalesStyle/desc/']

	#Defining rule to crawl next pages

	rules = (Rule(LinkExtractor(restrict_xpaths = ['//*[@id="searchResults"]/a']),follow=True,callback='parse_data'),
			 Rule(LinkExtractor(restrict_xpaths = ['//*[@id="resultWrap"]/div/div/a']),follow=True,callback='parse_data'),)


	def parse_data(self,response):
		shoe_link = response.xpath('//*[@id="searchResults"]/a/@href').extract()
		brand_name = response.xpath('//*[@id="prdImage"]/h1/a/text()').extract()
		shoe_name = response.xpath('//*[@id="prdImage"]/h1/a[2]/span/text()').extract()
		colorcode = response.xpath('//*[@id="color"]/option/@value').extract()
		colorway = response.xpath('//*[@id="color"]/option/text()').extract()
		topview = response.xpath('//*[@id="angle-1"]/@href').extract()
		bottomview = response.xpath('//*[@id="angle-2"]/@href').extract()
		lateralfrontleft = response.xpath('//*[@id="angle-3"]/@href').extract()
		heelview = response.xpath('//*[@id="angle-4"]/@href').extract()
		medialfrontright = response.xpath('//*[@id="angle-5"]/@href').extract()
		toeview = response.xpath('//*[@id="angle-6"]/@href').extract()

		for brand, shoe, top, bottom, lateral, heel, medial, toe in zip(brand_name, shoe_name, topview, bottomview, lateralfrontleft, heelview, medialfrontright, toeview):
			item = ZapposcrapeItem()
			abs_url = response.urljoin(shoe_link)
			item['shoe_link'] = abs_url
			item['brand_name'] = brand
			item['shoe_name'] = shoe
			item['topview'] = 'www.zappos.com' + str(top)
			item['bottomview'] = 'www.zappos.com' + str(bottom)
			item['lateralfrontleft'] = 'www.zappos.com' + str(lateral)
			item['heelview'] = 'www.zappos.com' + str(heel)
			item['medialfrontright'] = 'www.zappos.com' + str(medial)
			item['toeview'] = 'www.zappos.com' + str(toe)

			item['colorcode'] = abs_url.rsplit('color/')[-1]
			temp_dict = zip((code for code in colorcode), (color for color in colorway))
			for key, value in temp_dict:
				if key in item['colorcode']:
					item['colorway'] = value

			yield item
