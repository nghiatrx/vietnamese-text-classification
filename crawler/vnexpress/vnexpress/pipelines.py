# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class VnexpressPipeline(object):

    count = 22487

    def process_item(self, item, spider):
        data = item['title'] + ' ' + item['description'] + item['body']
        data = data.strip()
        
        if len(data) > 50:
            file = open('../../data/' + item['category'] + '/' + str(self.count) + '.txt', 'w+')
            file.write(data)
            file.close()
            self.count += 1
        return item

