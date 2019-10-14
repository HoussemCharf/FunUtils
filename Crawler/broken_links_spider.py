from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item, Field


class BrokenItem(Item):
    url = Field()
    referer = Field()
    status = Field()


class BrokenLinksSpider(CrawlSpider):
    name = "404Crawler"
    allowed_domains = ["example.com"]
    start_urls = ["https://www.example.com"]
    handle_httpstatus_list = [404]
    rules = (Rule(SgmlLinkExtractor(), callback='parse_item', follow=True),)

    def parse_item(self, response):
        if response.status == 404:
            item = BrokenItem()
            item['url'] = response.url
            item['referer'] = response.request.headers.get('Referer')
            item['status'] = response.status

            # Open database connection
            db = MySQLdb.connect("localhost","test","test","test")
            table = 'zz_' + self.projekt_id + '_404'
            
            # prepare a cursor object using cursor  method
            cursor = db.cursor() 
            sql = """INSERT INTO """ + table + """
            (
                url, prev_page, prev_link_url, prev_link_text, status
            ) 
            VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (item['url'], item['referer'], item['referer'], item['link_text'], item['status'], ))
            db.commit()
            db.close()

            return item
