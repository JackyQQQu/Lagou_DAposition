# coding:utf-8

import numpy as np
import pandas as pda
import matplotlib.pyplot as pp
import matplotlib.pylab as pyl
import re

pp.rcParams['font.sans-serif'] = ['SimHei']   # 用来正常显示中文标签
pp.rcParams['axes.unicode_minus'] = False   # 用来正常显示负号
# 读取数据
data = pda.read_excel("E:\\编程学习\\Project\\lagou\\lagouposition.xlsx")
data1 = data.T
print(len(data))

# 数据清洗,去除缺失值
salary = data1.values[8]
city = data1.values[3]
companySize = data1.values[5]
for i in range(0, len(data)):
    if len(salary[i] or city[i] or companySize[i]) == 0:
        data.drop(i, axis=0, inplace=True)

# 通过饼图分析需求数据分析岗位的公司发展情况所占比例
financestage = data1.values[6]
la1 = u"不需要融资", u"未融资", u"天使轮"
la2 = u"A轮", u"B轮", u"C轮", u"D轮及以上"
la3 = u"初创型公司", u"发展型公司", u"上市公司"

fs_data1 = np.array(range(len(la1)))
i1, i2, i3 = 0, 0, 0
for fst1 in la1:
    fs_data1[i1] = np.sum(financestage == fst1)
    i1 += 1
fs_data1_1 = np.array(fs_data1)
fs_data1_1 = fs_data1_1.sum()
fs_data1 = fs_data1/fs_data1_1

fs_data2 = np.array(range(len(la2)))
for fs2 in la2:
    fs_data2[i3] = np.sum(financestage == fs2)
    i3 += 1
fs_data2_1 = np.array(fs_data2)
fs_data2_1 = fs_data2_1.sum()
fs_data2 = fs_data2/fs_data2_1

fs_data3 = np.array(range(len(la3)))
fs_data3[0] = fs_data1_1
fs_data3[1] = fs_data2_1
fs_data3[2] = np.sum(financestage == "上市公司")
fs_data3 = fs_data3/len(financestage)
explode1 = (0, 0, 0.)
explode2 = (0, 0, 0, 0)
explode3 = (0, 0.1, 0)

# 分析数据分析岗位对不同学历所占的比重
education = data1.values[7]
ed = education.tolist()
ed_s = set(ed)
ed_data = np.array(range(len(ed_s)))
i4 = 0
labels4 = []
for edt in ed_s:
    ed_data[i4] = np.sum(education == edt)
    labels4.append(edt)
    i4 += 1
ed_data = ed_data/len(education)
explode4 = (0, 0, 0, 0, 0)
# 分析数据分析岗位对不同工作年限所占的比重
workYear = data1.values[11]
wy = workYear.tolist()
wy_s = set(wy)
wy_data = np.array(range(len(wy_s)))
i5 = 0
labels5 = []
for wyt in wy_s:
    wy_data[i5] = np.sum(workYear == wyt)
    labels5.append(wyt)
    i5 += 1
wy_data = wy_data/len(workYear)
explode5 = (0, 0, 0, 0, 0, 0)

# pp.pie(wy_data, explode=explode5, autopct="%1.1f%%", labels=labels5, startangle=90, radius=1)
# pp.axis("equal")
# pp.show()
# pp.savefig('E:\\编程学习\\Project\\lagou\\p5.png', format='png', bbox_inches='tight', transparent=True, dpi=600)

# 分析不同规模企业所占的比重
cs = companySize.tolist()
cs_s = set(cs)
cs_data = np.array(range(len(cs_s)))
cs_width = np.arange(len(cs_data))
i6 = 0
labels6 = []
for cst in cs_s:
    cs_data[i6] = np.sum(companySize == cst)
    labels6.append(cst)
    i6 += 1

# pyl.barh(cs_width, cs_data, color="g", height=0.5)
# pyl.yticks(cs_width, labels6)
# pyl.show()
# pyl.savefig('E:\\编程学习\\Project\\lagou\\p6.png', format='png', bbox_inches='tight', transparent=True, dpi=600)

# 分析不同城市对于数据分析职位的需求量
cy = city.tolist()
cy_s = set(cy)
cy_data = np.array(range(len(cy_s)))
cy_width = np.arange(len(cy_data))
i7 = 0
labels7 = []
for cyt in cy_s:
    cy_data[i7] = np.sum(city == cyt)
    labels7.append(cyt)
    i7 += 1
# 分析需求数据分析职位的企业所从事的领域
industryField = data1.values[4]
idf = industryField.tolist()
idf = ",".join(idf)
idf = re.split("、|,| ", idf)
while '' in idf:
    idf.remove('')
idf = np.array(idf)
idf_s = set(idf)
idf_data = np.array(range(len(idf_s)))
idf_width = np.arange(len(idf_data))
i8 = 0
labels8 = []
for itf in idf_s:
    idf_data[i8] = np.sum(idf == itf)
    labels8.append(itf)
    i8 += 1

# pyl.bar(cy_width, cy_data, color="b")
# pyl.xticks(cy_width, labels7)
# pyl.show()
# pyl.savefig('E:\\编程学习\\Project\\lagou\\p8.png', format='png', bbox_inches='tight', transparent=True, dpi=600)

# 分析不同薪资所占的分布情况
salary = data1.values[8]
# 分割薪资为最大值和最小值
sy_1 = []
for i9 in range(0, len(salary)):
    sy_1.append(re.split("-", salary[i9]))
sy_min = []
sy_max = []
for sy_2 in sy_1:
    # print(sy_2[1])
    # sy_min.append(sy_2[0])
    sy_max.append(sy_2[1])
# print(sy_min, sy_max)
# print(len(sy_1))


'''
for i in range(0, len(financestage)):
    if financestage[i] == "不需要融资":
        financestage[i] = 0
    if financestage[i] == "未融资":
        financestage[i] = 1
    if financestage[i] == "天使轮":
        financestage[i] = 2
    if financestage[i] == "A轮":
        financestage[i] = 3
    if financestage[i] == "B轮":
        financestage[i] = 4
    if financestage[i] == "C轮":
        financestage[i] = 5
    if financestage[i] == "D轮及以上":
        financestage[i] = 6
    if financestage[i] == "上市公司":
        financestage[i] = 7
'''