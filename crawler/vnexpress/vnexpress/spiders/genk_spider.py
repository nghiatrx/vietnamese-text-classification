import scrapy

def urls(page_to=1, page_from=10):
    result = []
    for i in range(page_to, page_from):
        result.append('http://genk.vn/ajax-cate/page-' + str(i) + '-c211/20181125103715845__20181123153409736__20181124025209908.chn')
    return result

urlPrefix = 'http://genk.vn'


class GenkNewsSpider(scrapy.Spider):
    name = 'genk'
    allowed_domains = ['genk.vn']
    start_urls = urls(page_to=800, page_from=1136)

    def parse(self, response):
        for article in response.css('li.knswli'):
            url = urlPrefix + article.css('h4.knswli-title>a::attr(href)').extract_first()
            yield scrapy.Request(url, callback=self.parse_contents)


    def parse_contents(self, response):
        title = response.css('h1.kbwc-title::text').extract_first()
        if title is not None:
            title = title.replace('\n', '').replace('\t', '').strip()
        else:
            title = ''

        description = response.css('h2.knc-sapo::text').extract_first()
        if description is not None:
            description = description.replace('\n', '').replace('\t', '').strip()
        else:
            description = ''


        body = ''

        try:
            for p in response.css('div.knc-content p:not(.VCSortableInPreviewModeWrapper)'):
                temp = p.css('::text').extract_first()
                if temp is not None:
                    body += temp.strip() + ' '
        except ValueError:
            pass

        body = body.replace('\n', ' ').replace('\xa0', '').replace('\t', '').strip()

        yield {'title': title, 'description': description, 'body': body, 'category': 'sohoa'}








