import scrapy
from ..items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
	name="quotes"
	page_number=2
	start_urls=["https://quotes.toscrape.com/"]

	def parse(self, response):
		all_div_quotes=response.css('div.quote')

		items=QuotetutorialItem()

		for quotes in all_div_quotes:
			title=quotes.css('span.text::text').extract()
			author=quotes.css('.author::text').extract()
			tag=quotes.css('a.tag::text').extract()

			# checklove=False
			# for i in tag:
			# 	if(i=='love'):
			# 		checklove=True

			items['title']=title
			items['author']=author
			items['tag']=tag


			yield items

		next_page="https://quotes.toscrape.com/page/"+str(QuotesSpider.page_number)+"/"
		if QuotesSpider.page_number<=11:
			QuotesSpider.page_number+=1
			yield response.follow(next_page, callback=self.parse)
