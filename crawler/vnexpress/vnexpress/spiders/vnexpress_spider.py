import scrapy


def urls(page_to=1, page_from=10):
    result = []
    for i in range(page_to, page_from):
        result.append('https://vnexpress.net/tin-tuc/oto-xe-may/page/' + str(i) + '.html')
    return result


class VnexpressSpider(scrapy.Spider):
    name = 'vnexpress'
    allowed_domains = ['vnexpress.net']
    start_urls = urls(page_to=401, page_from=1000)

    def parse(self, response):
        for title in response.css('section.container article.list_news h3.title_news>a:not(.icon_commend)'):
            url = title.css('::attr(href)').extract_first()
            yield scrapy.Request(url, callback=self.parse_contents)

    def parse_contents(self, response):
        title = response.css('h1.title_news_detail::text').extract_first()
        if title is not None:
            title = title.replace('\n', '').replace('\t', '').strip()
        else:
            title = ''

        description = response.css('h2.description::text').extract_first()
        if description is not None:
            description = description.replace('\n', '').replace('\t', '').strip()
        else:
            description = ''

        body = ''

        try:
            for p in response.css('article.content_detail p'):
                temp = p.css('::text').extract_first()
                if temp is not None:
                    body += temp.strip() + ' '
        except ValueError:
            pass

        body = body.replace('\n', ' ').replace('\xa0', '').replace('\t', '').strip()

        try:
            for p in response.css('article.desc_cation'):
                temp = p.css('p::text').extract_first()
                if temp is not None:
                    body += temp.strip() + ' '
        except ValueError:
            pass

        body = body.replace('\n', ' ').replace('\xa0', '').replace('\t', '').strip()

        yield {'title': title, 'description': description, 'body': body, 'category': 'xe'}
