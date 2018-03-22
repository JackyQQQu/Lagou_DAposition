# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class LagouPipeline(object):
    def process_item(self, item, spider):
        positionname = item['positionName']  # 职位
        companyname = item['companyName']  # 公司名
        city = item['city']  # 工作地点
        industryfield = item['industryField']  # 公司所在领域及从事内容
        companysize = item['companySize']  # 公司规模(人数）
        financestage = item['financeStage']  # 融资情况
        education = item['education']  # 学历要求
        salary = item['salary']  # 薪资
        companylabellist = item['companyLabelList']  # 福利待遇
        firsttype = item['firstType']  # 类型
        workyear = item['workYear']  # 工龄
        positionadvantage = item['positionAdvantage']  # 职位诱惑
        positionlables = item['positionLables']  # 标签
        # print(positionname, companyname, city, salary)
        conn = pymysql.connect("localhost", "root", "7758258", "lagou", use_unicode=True, charset="utf8")
        sql = "insert into dataanalysis(positionName,companyFullName,city,industryField,companySize,financeStage," \
              "education,salary,companyLabelList,firstType,workYear,positionAdvantage,positionLables)" \
              " values('" + positionname + "','" + companyname + "','" + city + "','" + industryfield + "','" + companysize + "','" + financestage + "','" + education + "','" + salary + "','" + companylabellist + "','" + firsttype + "','" + workyear + "','" + positionadvantage + "','" + positionlables + "')"
        conn.query(sql)
        conn.commit()
        conn.close()
        return item

        


