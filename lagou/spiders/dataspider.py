# -*- coding: utf-8 -*-
import scrapy
from lagou.items import LagouItem
from scrapy.http import FormRequest
import json
from fake_useragent import UserAgent
import math


class DataspiderSpider(scrapy.Spider):
    name = 'dataspider'
    allowed_domains = ['lagou.com']
    urls = ['https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=0']
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?'
                   'px=default',
    }
    cookies = {
        'cookies':
        '_ga=GA1.2.297812503.1521544718; _gid=GA1.2.2085758879.1521544718; '
        'user_trace_token=20180320191838-6fd479b7-2c30-11e8-b546-5254005c3644;'
        ' LGUID=20180320191838-6fd47d12-2c30-11e8-b546-5254005c3644; ab_test_random_num=0; '
        'showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0;'
        ' JSESSIONID=ABAAABAABEEAAJAD3D17E51A4FCA2465529628CD6940CBC; '
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521611278,1521623941,1521623957,1521705067; '
        'LGSID=20180322155109-c8ddde3c-2da5-11e8-9415-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; '
        'PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DA16DHItcwNNlMqjYggldtXhVFTwLvpXl7YMoP21Q3'
        'GW%26wd%3D%26eqid%3D8f84882b00029c09000000055ab36065; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _'
        'putrc=9C3E560C302F2274; login=true; unick=%E7%9E%BF%E6%99%A8; gate_login_token=023e0943fac774a8d67fb'
        '2db92050f239eb6ea541b0ae95a; LGRID=20180322155158-e5b222e3-2da5-11e8-b573-5254005c3644; Hm_l'
        'pvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521705116; TG-TRACK-CODE=search_code; '
        'SEARCH_ID=fc93ee755bbd42f2a40adc2bf201a659; index_location_city=%E5%8C%97%E4%BA%AC'
    }
    page = 1
    form_data = {
        'first': 'true',
        'city': '苏州',
        'pn': str(page),  # 页数
        'kd': '数据分析',  # 关键词
    }

    def start_requests(self):
        # citys = ["北京", "上海", "深圳", "杭州", "广州", "南京", "成都", "武汉", "西安", "苏州"]
        print("------测试抓取第"+str(self.page)+"页------")
        return [
            FormRequest(
                url=self.urls[0],
                headers=self.headers,
                formdata=self.form_data,
                encoding='utf-8',
                method='POST',
                cookies=self.cookies,
                callback=self.parse
            )
        ]

    def parse(self, response):
        item = LagouItem()
        result = json.loads(response.body)
        # print(result)
        infs = result['content']["positionResult"]['result']
        # print(infs)
        for inf in infs:
            try:
                item['positionName'] = "".join(inf['positionName'])  # 职位
                item['companyName'] = "".join(inf['companyShortName'])  # 公司名
                item['city'] = "".join(inf['city'])  # 工作地点
                item['industryField'] = "".join(inf['industryField'])  # 公司所在领域及从事内容
                item['companySize'] = "".join(inf['companySize'])  # 公司规模(人数）
                item['financeStage'] = "".join(inf['financeStage'])  # 融资情况
                item['education'] = "".join(inf['education'])  # 学历要求
                item['salary'] = "".join(inf['salary'])  # 薪资
                item['companyLabelList'] = "".join(inf['companyLabelList'])  # 福利待遇
                item['firstType'] = "".join(inf['firstType'])  # 类型
                item['workYear'] = "".join(inf['workYear'])  # 工龄
                item['positionAdvantage'] = "".join(inf['positionAdvantage'])  # 职位诱惑
                item['positionLables'] = "".join(inf['positionLables'])  # 标签
                # print(item['companyName'], item['salary'])
                yield item
            except Exception as e:
                print(e)
        # 翻页
        page_count = result['content']["positionResult"]["totalCount"]/15
        if page_count > 30:
            page_count = 30
        if self.page < page_count:
            self.page += 1
            count = page_count
            count = math.ceil(count-self.page)
            print("------正在抓取第" + str(self.page) + "页，还有" + str(count) + "页未获取------")
            yield FormRequest(
                    url=self.urls[0],
                    headers=self.headers,
                    formdata={
                        'first': 'true',
                        'city': '苏州',
                        'pn': str(self.page),  # 页数
                        'kd': '数据分析',  # 关键词
                    },
                    encoding='utf-8',
                    method='POST',
                    cookies=self.cookies,
                    callback=self.parse,
                    dont_filter=True
                    )




