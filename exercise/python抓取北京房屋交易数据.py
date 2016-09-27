# -*- coding: UTF-8 -*-    或者  #coding=utf-8
import json
import re
import sys
import time
import urllib

import leancloud
from leancloud import LeanCloudError
from leancloud import Object

'''
原文: http://mushuichuan.com/2016/03/25/python-house/
'''
class HouseParser:
    def __init__(self):
        self.Url = "http://www.bjjs.gov.cn/tabid/2167/default.aspx?COLLCC=2389390305&COLLCC=2937872865&"
        self.jsonBean = {}
        self.commercial_title = ['可售期房统计', '预售许可', '期房网上认购', '期房网上签约', '未签约现房统计', '现房项目情况',
                                 '现房网上认购', '现房网上签约']
        self.stock_title = ['可售房源统计', '新发布房源', '存量房网上签约', '存量房网上签约']

    def print_str(self, s):
        type = sys.getfilesystemencoding()
        print (s.decode('UTF-8').encode(type))

    def get(self, url):
        request = urllib.request.Request(url);
        try:
            response = urllib.request.urlopen(request)
            read = response.read()
            return read
        except urllib.request.HTTPError as e:
            print('Get content failed:', e.code)
            return

    def read_content(self):
        print('Get content from Net.')
        # with open("content.txt", 'r') as f:
        #     content = f.read().decode('utf-8')
        content = self.get(self.Url).decode('utf-8')
        if content:
            # remove &nbsp
            pattern = re.compile(r'&nbsp;')
            txt = pattern.sub(" ", content)
            print('Get content success.')
            return txt
        else:
            return

    def parse(self):
        content = self.read_content()
        if content:
            print('Start to parse content')
            commercial_bean = {}
            pattern = re.compile(r'<tr[^<>]+><td[^<>]+><span[^<>]+>([^<>]+)</span>')
            date = pattern.search(content)
            if date:
                commercial_bean['date'] = date.group(1)
                self.jsonBean['t'] = time.mktime(time.strptime(date.group(1), '%Y-%m-%d')) * 1000

            commercial = re.findall(
                r'<tr[^<>]+><td[^<>]+>([^<>(：]+).*</td>\s+<td[^<>]+><span [^<>]+>([^<>]+).*</span></td></tr>',
                content)
            if commercial:
                items_queue = []
                for i in range(8):
                    item = {}
                    detail = {}
                    item['count'] = commercial[i * 10][0] + ":" + commercial[i * 10][1]
                    item['title'] = self.commercial_title[i]
                    item['area'] = commercial[i * 10 + 1][0] + ":" + commercial[i * 10 + 1][1]
                    detail['houC'] = commercial[i * 10 + 2][0] + ":" + commercial[i * 10 + 2][1]
                    detail['houA'] = commercial[i * 10 + 3][0] + ":" + commercial[i * 10 + 3][1]
                    detail['comC'] = commercial[i * 10 + 4][0] + ":" + commercial[i * 10 + 4][1]
                    detail['comA'] = commercial[i * 10 + 5][0] + ":" + commercial[i * 10 + 5][1]
                    detail['offC'] = commercial[i * 10 + 6][0] + ":" + commercial[i * 10 + 6][1]
                    detail['offA'] = commercial[i * 10 + 7][0] + ":" + commercial[i * 10 + 7][1]
                    detail['carC'] = commercial[i * 10 + 8][0] + ":" + commercial[i * 10 + 8][1]
                    detail['carA'] = commercial[i * 10 + 9][0] + ":" + commercial[i * 10 + 9][1]
                    item['detail'] = detail
                    items_queue.append(item)
                commercial_bean['items'] = items_queue
                self.jsonBean['c'] = commercial_bean
            stock = re.findall(
                r'<tr[^<>]+>\s*<td[^<>]+>([^<>(：]+).*\s+</td>\s+<td[^<>]+>\s+<span[^<>]+>([^<>]+)</span>\s+',
                content)
            if stock:
                stock_bean = {}
                item_queue = []
                for i in range(4):
                    item = {}
                    item['tit'] = self.stock_title[i]
                    item['cou'] = stock[i * 4][0].strip() + ":" + stock[i * 4][1].strip()
                    item['area'] = stock[i * 4 + 1][0].strip() + ":" + stock[i * 4 + 1][1].strip()
                    item['cou2'] = stock[i * 4 + 2][0].strip() + ":" + stock[i * 4 + 2][1].strip()
                    item['area2'] = stock[i * 4 + 3][0].strip() + ":" + stock[i * 4 + 3][1].strip()
                    item_queue.append(item)
                stock_bean['items'] = item_queue
                self.jsonBean['s'] = stock_bean
            jsonstr = json.dumps(self.jsonBean)
            print ('Parse complete.')
            self.update_data(jsonstr)
            # with open("result.txt", 'w') as f:
            #     f.write(jsonstr.encode('utf8'))

    def update_data(self, data):
        print ('Update data to server')
        JSON_TNAME = "JSON_TNAME";
        JSON_DATE = "JSON_DATE"
        JSON_TIME = "JSON_TIME"
        JSON_CONTENT = "JSON_CONTENT"
        leancloud.init("hgRblSfMhkqj2oJzS3hNMw00-gzGzoHsz", "Yxi3qfSgA3AYh1JOapAPTxsO")
        BeanObj = Object.extend(JSON_TNAME)
        leanObj = BeanObj()

        leanObj.set('JSON_DATE', self.jsonBean['c']['date'])
        leanObj.set('JSON_TIME', int(self.jsonBean['t']))
        leanObj.set('JSON_CONTENT', data)
        try:
            leanObj.save()
            print ('Update success.')
        except LeanCloudError as e:
            print ('update failed' + e)


if __name__ == '__main__':
    print('Start to run.')
    parser = HouseParser()
    parser.parse()
