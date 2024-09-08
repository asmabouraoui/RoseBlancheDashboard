import scrapy

from food_sc.items import FoodItem


class FoodspiderSpider(scrapy.Spider):
    name = "foodspider"
    allowed_domains = ["www.feedtables.com"]
    start_urls = ["https://www.feedtables.com/"]
    FoodItem = FoodItem()

    def parse(self, response):
        name=response.css('div.feed-title-home::text').getall()
        foods = response.css('table td.views-field').getall()
        
        print(foods)
        for food in foods :

            # Convert the string to a Selector
            food_selector = scrapy.Selector(text=food)
            anchor_tag = food_selector.css(
                'a').get()  # Select the first <a> tag
            if anchor_tag:
                relative_url = food_selector.css('a::attr(href)').get()
                yield response.follow('https://www.feedtables.com/'+relative_url, callback=self.parse_food_page,meta={'name': name})


    def parse_food_page(self, response):
        name = response.meta['name']

        yield {
            'df': response.css('h2.bd-container-29 ::text').get(),
            'lines':response.css('div.feed-icon a::attr(href)').get(),
            'name':name
         
        }
