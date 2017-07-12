import scrapy
from nikescrape.items import SkatescrapeItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as bs

class SkatescrapeSpider(CrawlSpider):

	name = 'SkateCrawl'
#	handle_httpstatus_all = True
	start_urls = ['http://www.skatewarehouse.com/menshoes.html?view_all=true']

	#Defining rule to crawl next pages

	rules = (Rule(LinkExtractor(restrict_xpaths = ['//*[@id="content_wrap"]/div/ul/li/div/div/div/a']),follow=True,callback='parse_data'),)


	def parse_data(self,response):
		shoe_name = response.xpath('//*[@id="content_wrap"]/div[2]/div[2]/div[1]/h1/text()').extract()
		colorway = response.xpath('//*[@id="content_wrap"]/div[2]/div[2]/div[1]/h1/span/text()').extract()
		topview = response.xpath('//*[@id="multiview"]/li[4]/a/img/@src').extract()
		bottomview = response.xpath('//*[@id="multiview"]/li[5]/a/img/@src').extract()
		lateralfrontleft = response.xpath('//*[@id="multiview"]/li[2]/a/img/@src').extract()
		medialfrontright = response.xpath('//*[@id="multiview"]/li[3]/a/img/@src').extract()

		for shoe, color, top, bottom, lateral, medial in zip(shoe_name, colorway, topview, bottomview, lateralfrontleft, medialfrontright):
			item = SkatescrapeItem()
#			abs_url = response.urljoin(shoe_link)
#			item['shoe_link'] = abs_url
#			item['brand_name'] = abs_url.rpslit(' ')[1]
			item['shoe_name'] = shoe
			item['colorway'] = color
			item['topview'] = top.rsplit('&')[0]
			item['bottomview'] = bottom.split('&')[0]
			item['lateralfrontleft'] = lateral.split('&')[0]
			item['medialfrontright'] = medial.split('&')[0]



			yield item
