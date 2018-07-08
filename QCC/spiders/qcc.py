# -*- coding: utf-8 -*-
import scrapy
import time
from trans_cookie import trans_cookie
from user_agents import MY_USER_AGENT
from provinces import provinces, provinces_dict


class QccSpider(scrapy.Spider):
    name = 'qcc'
    # allowed_domains = ['www']
    provinces = provinces
    print('各省对应的简称如下：')
    for i in range(8):
        print(list(provinces_dict.items())[4 * i: 4 * i + 4] )
    print('请输入要爬取的省份的简称：（例如：AH）')
    province = input()
    print('请输入要爬取的页码范围：（例如：1-20）')
    pages = [int(i) for i in input().split('-')]

    with open('cookies.txt', 'r') as f:
        cookie_lst = f.readlines()
    f.close()

    num_cookie = 0
    def cookie_next(self):
        self.cookie = self.cookie_lst[self.num_cookie % len(self.cookie_lst)]
        self.num_cookie += 1
        return trans_cookie(self.cookie)

    num_user_agent = 0
    def headers_next(self):
        n = len(MY_USER_AGENT)
        self.headers = {
            'Connection': 'keep - alive',  # 保持链接状态
            'User-Agent': MY_USER_AGENT[self.num_user_agent % n]
        }
        self.num_user_agent += 1
        return self.headers


    def start_requests(self):
        for i in range(self.pages[0], self.pages[1] + 1):
            time.sleep(2)
            yield scrapy.Request(
                url='https://www.qichacha.com/g_%s_%d.html' % (self.province, i),
                headers=self.headers_next(),
                cookies=self.cookie_next(),
                callback=self.parse_firm_url)


    def parse_firm_url(self, response):
        url = 'https://www.qichacha.com'
        url_lst = response.css('.panel-default').css('a').xpath('@href').extract()
        for i in range(10):
            time.sleep(2)
            yield scrapy.Request(
                url=url + url_lst[i],
                headers=self.headers_next(),
                cookies=self.cookie_next())

    def parse(self, response):
        dic = {}
        title = response.css('.content').css('.title').css('h1').extract()[0].split('>')[1].split('<')[0]
        content = response.css('.content').css('.cvlu')
        if len(content) > 4:
            phone = content[1].css('span').xpath('text()').extract()[-1].strip()
            web_site = content[2].css('a').xpath('@href').extract()[2].strip()
            try:
                mail = content[3].css('a').xpath('text()').extract()[0].strip()
            except:
                mail = content[3].xpath('text()').extract()[0].strip()
            address = content[4].css('a')[0].xpath('text()').extract()[0].strip()
        else:
            phone = content[0].css('span').xpath('text()').extract()[-1].strip()
            web_site = content[1].xpath('text()').extract()[0].strip()
            try:
                mail = content[2].css('a').xpath('text()').extract()[0].strip()
            except:
                mail = content[2].xpath('text()').extract()[0].strip()
            address = content[3].css('a')[0].xpath('text()').extract()[0].strip()

        dic['公司名称'] = title
        dic['电话'] = phone
        dic['官网'] = web_site
        dic['邮箱'] = mail

        tbody = response.css('.ntable').css('tr').css('td').xpath('text()').extract()

        body_lst = []
        for item in tbody:
            if item.strip() != '':
                body_lst.append(item.strip())
        for item in body_lst:
            if '注册资本：'  == item:
                start = body_lst.index(item)
            if '经营范围：' == item:
                end = body_lst.index(item) + 2

        body = body_lst[start: end]

        keys = ['注册资本：', '实缴资本：', '经营状态：', '成立日期：',
                '统一社会信用代码：', '纳税人识别号：', '注册号：', '组织机构代码：',
                '公司类型：', '所属行业：', '核准日期：', '登记机关：',
                '所属地区：', '英文名：', '曾用名', '参保人数', '人员规模',
                '营业期限', '企业地址：', '经营范围：']

        cn = 0
        while True:
            if body[cn].strip() in keys and body[cn + 1].strip() not in keys:
                dic[body[cn].strip()] = body[cn + 1].strip()
                cn += 2
            else:
                dic[body[cn]] = '-'
                cn += 1
            if cn >= len(body):
                break

        dic[self.province] = self.pages
        yield dic
