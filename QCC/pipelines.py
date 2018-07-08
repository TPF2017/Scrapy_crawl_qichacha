# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
from provinces import provinces_dict


class QccPipeline(object):
    def process_item(self, item, spider):
        return item



class QccInfoPipeline(object):

    def open_spider(self, spider):
        self.col = ['公司名称', '电话', '官网', '邮箱',
    '注册资本', '实缴资本', '经营状态', '成立日期',
    '统一社会信用代码', '纳税人识别号', '注册号',
    ' 组织机构代码',  '公司类型', '所属行业',
    '核准日期', '登记机关', '所属地区',
    '英文名',  '曾用名', '参保人数',
    '人员规模',  '营业期限', '企业地址', '经营范围']
        self.data = pd.DataFrame(columns=self.col)

    def process_item(self, item, spider):
        self.info = list(item.items())[-1]
        self.temp_data = pd.DataFrame.from_dict(
            dict(list(item.items())[: -1]), orient='index').T
        self.temp_data.columns = self.col
        self.data = pd.concat([self.data, self.temp_data])
        return item

    def close_spider(self, spider):
        self.data.to_excel('企查查_%s_%d-%d.xlsx' % (provinces_dict[self.info[0]], self.info[1][0], self.info[1][1]), index=False)
