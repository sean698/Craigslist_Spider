import scrapy

class CragSpider(scrapy.Spider):
    name = 'crag'
    allowed_domains = ['vancouver.craigslist.org']

    def __init__(self, category):
        self.start_urls = [category]

    def parse(self, response):
        listings = response.xpath('//*[@class="result-row"]')
        for listing in listings:
            date = listing.xpath('.//*[@class="result-date"]/text()').extract_first()
            link = listing.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
            title = listing.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()

            yield scrapy.Request(link,
                                callback=self.parse_listings,
                                meta={
                                    'date': date,
                                    'link': link,
                                    'title': title
                                })
        
        next_page_url = response.xpath('//*[@class="button next"]/@href').extract_first()
        if next_page_url:
            absolute_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_url, callback=self.parse)

    def parse_listings(self, response):
        date = response.meta['date']
        link = response.meta['link']
        title = response.meta['title']
        images = response.xpath('//div[@id="thumbs"]/a/@href').extract()
        description = response.xpath('//section[@id="postingbody"]/text()').extract()

        yield {
            'date': date,
            'title': title,
            'link': link,
            'description' : description,
            'images': images
        }