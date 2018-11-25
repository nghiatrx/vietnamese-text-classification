import scrapy

def urls(page_to=1, page_from=10):
    result = []
    for i in range(page_to, page_from):
        result.append('http://vietnamnet.vn/vn/chuyen-trang/oto-xemay/trang' + str(i) + '/')
    return result

urlPrefix = 'http://vietnamnet.vn'

exceptStrings = [
    '10 clip',
    'clip nóng'
]

class GenkNewsSpider(scrapy.Spider):
    name = 'vietnamnet'
    allowed_domains = ['vietnamnet.vn']
    start_urls = urls(page_to=100, page_from=130)

    def parse(self, response):
        for article in response.css('div.HomeBlock li.item'):
            url = urlPrefix + article.css('a::attr(href)').extract_first()
            yield scrapy.Request(url, callback=self.parse_contents)

    def parse_contents(self, response):
        title = response.css('div.ArticleDetail h1.title::text').extract_first()
        if title is not None:
            title = title.replace('\n', '').replace('\t', '').strip()
        else:
            title = ''

        body = ''
        try:
            for p in response.css('div.ArticleContent p'):
                temp = p.css(' ::text').extract_first()
                if temp is not None:
                    body += temp.strip() + ' '
        except ValueError:
            pass

        body = body.replace('\n', ' ').replace('\xa0', '').replace('\t', '').strip()

        excepted = False
        for str in exceptStrings:
            if body.find(str) > -1:
                excepted = True

        if excepted is True:
            yield {'title': '', 'description': '', 'body': '', 'category': 'xe'}
        else:
            yield {'title': title, 'description': '', 'body': body, 'category': 'xe'}


        
