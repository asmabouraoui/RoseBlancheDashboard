import scrapy


class Food1spiderSpider(scrapy.Spider):
    name = "food1spider"
    allowed_domains = ["feedsdatabase.ilri.org"]
    start_urls = ["https://feedsdatabase.ilri.org/"]

    def parse(self, response):
        boxes = response.xpath(
            '//*[@id="block-tb-megamenu-menu-sub-saharan-africa-feed-com"]/div/div/ul/li').getall()
        for box in boxes:
            # Extract HTML content from the 'box' key
            selector = scrapy.Selector(text=box)  # Create a Selector object

            # Extract URL and type value
            url_link = selector.css('a::attr(href)').get()
            type_value = selector.css('a::text').get()

        # Yield the extracted data
            yield response.follow('https://feedsdatabase.ilri.org'+url_link, callback=self.parse_food1_page, meta={'type_value': type_value})

    def parse_food1_page(self, response):
        name = response.xpath('//*[@id="block-system-main"]/div/div[3]/div/ul/li/a')
        type_value = response.meta['type_value']
        for nom in name:
            url = nom.xpath("@href").get()
            nombre = nom.xpath("text()").get()
            yield response.follow('https://feedsdatabase.ilri.org'+url, callback=self.parse_food2_page,meta={'type_value': type_value, 'nombre': nombre})
            
    def parse_food2_page(self,response):
        type_value = response.meta['type_value']
        nombre = response.meta['nombre']
        csv_f=response.xpath('//*[@id="block-system-main"]/div/div[6]/a/@href').get()
        
        
        yield {
            'type_value': type_value,
            'nombre': nombre,
            'csv_f': csv_f
        }


