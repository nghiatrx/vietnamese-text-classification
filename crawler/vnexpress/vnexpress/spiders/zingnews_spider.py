import scrapy


def urls(page_to=1, page_from=10):
    result = []
    for i in range(page_to, page_from):
        result.append('https://news.zing.vn/oto-xe-may/trang' + str(i) + '.html')
    return result

urlPrefix = 'https://news.zing.vn'

class ZingNewsSpider(scrapy.Spider):
    name = 'zingnews'
    allowed_domains = ['news.zing.vn']
    start_urls = urls(page_to=1, page_from=50)

 
    def parse(self, response):
        for title in response.css('article.featured.text p.title'):
            url = urlPrefix + title.css('a::attr(href)').extract_first()
            yield scrapy.Request(url, callback=self.parse_contents)

    def parse_contents(self, response):
        title = response.css('section.main h1.the-article-title::text').extract_first()
        if title is not None:
            title = title.replace('\n', '').replace('\t', '').strip()
        else:
            title = ''

        description = response.css('section.main p.the-article-summary.cms-desc::text').extract_first()

        if description is not None:
            description = description.replace('\n', '').replace('\t', '').strip()
        else:
            description = ''

        body = ''

        try:
            for p in response.css('section.main div.the-article-body.cms-body p'):
                temp = p.css(' ::text').extract_first()
                if temp is not None:
                    body += temp.strip() + ' '
        except ValueError:
            pass

        body = body.replace('\n', ' ').replace('\xa0', '').replace('\t', '').strip()

        yield {'title': title, 'description': description, 'body': body, 'category': 'xe'}





