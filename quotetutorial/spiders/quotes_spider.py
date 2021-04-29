import scrapy
from scrapy.http import FormRequest
from ..items import QuotetutorialItem
from scrapy.utils.response import open_in_browser

class QuotesSpider(scrapy.Spider):
	# name="quotes"
	# start_urls=["https://quotes.toscrape.com/login"]
	#
	# def parse(self, response):
	# 	token=response.css("form input::attr(value)").extract_first()
	# 	return FormRequest.from_response(response,formdata={
	# 		'csrf_token' : token,
	# 		'username' : "sanjeetnaik11@gmail.com",
	# 		'password' : "helloworld"
	# 	},callback= self.start_scraping)
	#
	# def start_scraping(self,response):
	# 	open_in_browser(response)
	# 	all_div_quotes = response.css('div.quote')
	#
	# 	items = QuotetutorialItem()
	#
	# 	for quotes in all_div_quotes:
	# 		title = quotes.css('span.text::text').extract()
	# 		author = quotes.css('.author::text').extract()
	# 		tag = quotes.css('a.tag::text').extract()
	#
	# 		# checklove=False
	# 		# for i in tag:
	# 		# 	if(i=='love'):
	# 		# 		checklove=True
	#
	# 		items['title'] = title
	# 		items['author'] = author
	# 		items['tag'] = tag
	#
	# 		yield items
	name = "quotes"
	page_number = 2
	start_urls = ["https://quotes.toscrape.com/"]

	def parse(self, response):
		all_div_quotes = response.css('div.quote')

		items = QuotetutorialItem()

		for quotes in all_div_quotes:
			title = quotes.css('span.text::text').extract()
			author = quotes.css('.author::text').extract()
			tag = quotes.css('a.tag::text').extract()

			# checklove=False
			# for i in tag:
			# 	if(i=='love'):
			# 		checklove=True

			items['title'] = title
			items['author'] = author
			items['tag'] = tag

			yield items

		next_page = "https://quotes.toscrape.com/page/" + str(QuotesSpider.page_number) + "/"
		if QuotesSpider.page_number <= 11:
			QuotesSpider.page_number += 1
			yield response.follow(next_page, callback=self.parse)
