# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName = scrapy.Field()  # 职位
    companyName = scrapy.Field()  # 公司名
    city = scrapy.Field()  # 工作地点
    industryField = scrapy.Field()  # 公司所在领域及从事内容
    companySize = scrapy.Field()  # 公司规模(人数）
    financeStage = scrapy.Field()  # 融资情况
    education = scrapy.Field()  # 学历要求
    salary = scrapy.Field()  # 薪资
    companyLabelList = scrapy.Field()  # 福利待遇
    firstType = scrapy.Field()  # 类型
    workYear = scrapy.Field()  # 工龄
    positionAdvantage = scrapy.Field()  # 职位诱惑
    positionLables = scrapy.Field()  # 标签




