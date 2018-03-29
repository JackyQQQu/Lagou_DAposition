# coding:utf-8

import numpy as np
import pandas as pda
import matplotlib.pyplot as pp
import matplotlib.pylab as pyl
import re
# from Lagou_DAposition.apriori import *
import jieba
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

pp.rcParams['font.sans-serif'] = ['SimHei']   # 用来正常显示中文标签
pp.rcParams['axes.unicode_minus'] = False   # 用来正常显示负号
# 读取数据
data0 = pda.read_excel("E:\\编程学习\\Project\\lagou\\lagouposition.xlsx")
data1 = data0.T
# print(len(data0))

# 数据清洗,去除缺失值
salary = data1.values[8] # 薪酬
city = data1.values[3] # 城市
companySize = data1.values[5] # 公司规模
for i in range(0, len(data0)):
    if len(salary[i] or city[i] or companySize[i]) == 0:
        print(salary[i], city[i], companySize[i])
        data0.drop(i, axis=0, inplace=True)
data1 = data0.T
# print(len(data1))

# 通过饼图分析需求数据分析岗位的公司发展情况所占比例
financestage = data1.values[6]  # 融资情况
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
education = data1.values[7]  # 学历
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
explode4 = (0, 0, 0, 0, 0.1)
# 分析数据分析岗位对不同工作年限所占的比重
workYear = data1.values[11]  # 工作年限
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

pp.pie(wy_data, explode=explode5, autopct="%1.1f%%", labels=labels5, startangle=130, radius=1)
pp.axis("equal")

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
industryField = data1.values[4]  # 领域
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

# 分析不同薪资所占的分布情况
# 分割薪资为最大值和最小值
sy_1 = []
for i9 in range(0, len(salary)):
    sy_1.append(re.split("-", salary[i9]))
sy_min = []
sy_max = []
for sy_2 in sy_1:
    sy_2[0] = re.sub("\D", "", sy_2[0])
    if len(sy_2) < 2:
        sy_min.append(0)
        sy_max.append(sy_2[0])
    elif len(sy_2) == 2:
        sy_2[1] = re.sub("\D", "", sy_2[1])
        sy_min.append(sy_2[0])
        sy_max.append(sy_2[1])
# 求薪资平均值
sy_means = []
for i10 in range(0, len(sy_max)):
    sy_means.append((int(sy_max[i10]) + int(sy_min[i10]))/2)
sy_means = np.array(sy_means)
p = 0
for t in range(0, len(sy_means)):
    if 5 < sy_means[t] > 25:
        p += 1
# print(p/len(sy_means))
bins = np.arange(1, 80, 5)
# pyl.xlabel("平均薪资（单位：K）")
# pyl.hist(sy_means, bins, color="m", histtype="bar")

# 分析数据分析职位薪资水平和公司发展情况、学历水平、城市、工作年限之间的关联程度
# 处理公司发展水平信息
labels9 = {'不需要融资': 0, '未融资': 0, '天使轮': 0, 'A轮': 1, 'B轮': 1, 'C轮': 1, 'D轮及以上': 1, '上市公司': 1}
# 以A轮融资为分界
fs_ap = []
for la9_1 in financestage:
    for la9_2 in labels9:
        if la9_2 == la9_1:
            la9_1 = labels9[la9_2]
            fs_ap.append(la9_1)
fs_ap = np.array(fs_ap)
# 处理学历水平信息
# 以本科学历为分界
labels10 = {'不限': 0, '大专': 0, '本科': 1, '硕士': 1, '博士': 1}
ed_ap = []
for la10_1 in education:
    for la10_2 in labels10:
        if la10_2 == la10_1:
            la10_1 = labels10[la10_2]
            ed_ap.append(la10_1)
ed_ap = np.array(ed_ap)
# 处理城市信息
labels11 = {'北京': 1, '上海': 1, '深圳': 1, '广州': 1, '杭州': 1, '成都': 0, '武汉': 0, '南京': 0, '苏州': 0, '西安': 0}
# 定义北上广深杭为一类，其余为二类城市
cy_ap = []
for la11_1 in city:
    for la11_2 in labels11:
        if la11_2 == la11_1:
            la11_1 = labels11[la11_2]
            cy_ap.append(la11_1)
ed_ap = np.array(ed_ap)
# 处理工作年限信息
# 以1-3年工作年限为分界
labels12 = {'不限': 0, '应届毕业生': 0, '1年以下': 0, '1-3年': 1, '3-5年': 1, '5-10年': 1}
wy_ap = []
for la12_1 in workYear:
    for la12_2 in labels12:
        if la12_2 == la12_1:
            la12_1 = labels12[la12_2]
            wy_ap.append(la12_1)
wy_ap = np.array(wy_ap)
# 处理薪资信息
sy_ap = []
for la13 in sy_means:
    if la13 > 12.5:  # 以数量最多的10-15K的平均数为分界
        la13 = 1
    else:
        la13 = 0
    sy_ap.append(la13)

# 关联分析
# 数据集成
ap_data = pda.DataFrame([fs_ap, ed_ap, cy_ap, wy_ap, sy_ap])
ap_data = ap_data.T
ap_data.columns = ["发展情况", "学历", "城市", "工作年限", "薪资"]
# 总体关联计算
# find_rule(ap_data, 0.2, 0.5, "-->")

# 不同工作年限的薪资分布情况
la_wy = ['不限', '应届毕业生', '1年以下', '1-3年', '3-5年', '5-10年']
wy_sy = [[], [], [], [], [], []]
x = 0
for x1_1 in workYear:
    for x1_2 in la_wy:
        if x1_1 == x1_2:
            wy_sy[la_wy.index(x1_1)].append(sy_means[x])
    x += 1

wy_sy_df = pda.DataFrame(
    [
        pda.Series(wy_sy[0]),
        pda.Series(wy_sy[1]),
        pda.Series(wy_sy[2]),
        pda.Series(wy_sy[3]),
        pda.Series(wy_sy[4]),
        pda.Series(wy_sy[5])
    ]
).T
wy_sy_df.columns = la_wy
# wy_sy_df.boxplot()
# pp.ylabel("薪资水平（单位：K）")

# 不同学历的薪资分布情况
la_ed = ['不限', '大专', '本科', '硕士', '博士']
ed_sy = [[], [], [], [], []]
x = 0
for x2_1 in education:
    for x2_2 in la_ed:
        if x2_1 == x2_2:
            ed_sy[la_ed.index(x2_1)].append(sy_means[x])
    x += 1

ed_sy_df = pda.DataFrame(
    [
        pda.Series(ed_sy[0]),
        pda.Series(ed_sy[1]),
        pda.Series(ed_sy[2]),
        pda.Series(ed_sy[3]),
        pda.Series(ed_sy[4])
    ]
).T
ed_sy_df.columns = la_ed
# ed_sy_df.boxplot()
# pp.ylabel("薪资水平（单位：K）")

# 不同城市的薪资分布情况
la_cy = ['北京', '上海', '深圳', '广州', '杭州', '成都', '武汉', '南京', '苏州', '西安']
cy_sy = [[], [], [], [], [], [], [], [], [], []]
x = 0
for x3_1 in city:
    for x3_2 in la_cy:
        if x3_1 == x3_2:
            cy_sy[la_cy.index(x3_1)].append(sy_means[x])
    x += 1
cy_sy_df = pda.DataFrame(
    [
        pda.Series(cy_sy[0]),
        pda.Series(cy_sy[1]),
        pda.Series(cy_sy[2]),
        pda.Series(cy_sy[3]),
        pda.Series(cy_sy[4]),
        pda.Series(cy_sy[5]),
        pda.Series(cy_sy[6]),
        pda.Series(cy_sy[7]),
        pda.Series(cy_sy[8]),
        pda.Series(cy_sy[9]),
    ]
).T
cy_sy_df.columns = la_cy
# cy_sy_df.boxplot()
# pp.ylabel("薪资水平（单位：K）")

# 不同融资的薪资分布情况
la_fs = ['不需要融资', '未融资', '天使轮', 'A轮', 'B轮', 'C轮', 'D轮及以上', '上市公司']
fs_sy = [[], [], [], [], [], [], [], []]
x = 0
for x3_1 in financestage:
    for x3_2 in la_fs:
        if x3_1 == x3_2:
            fs_sy[la_fs.index(x3_1)].append(sy_means[x])
    x += 1
fs_sy_df = pda.DataFrame(
    [
        pda.Series(fs_sy[0]),
        pda.Series(fs_sy[1]),
        pda.Series(fs_sy[2]),
        pda.Series(fs_sy[3]),
        pda.Series(fs_sy[4]),
        pda.Series(fs_sy[5]),
        pda.Series(fs_sy[6]),
        pda.Series(fs_sy[7])
    ]
).T
fs_sy_df.columns = la_fs
# fs_sy_df.boxplot()
# pp.ylabel("薪资水平（单位：K）")

# pp.show()
# pp.savefig('E:\\编程学习\\Project\\lagou\\p5.png', format='png', bbox_inches='tight', transparent=True, dpi=600)

# 职位诱惑和标签词云
pic = imread("E:\\编程学习\\Project\\lagou\\pic.png")
wc = WordCloud(background_color='white',
               max_words=100,
               mask=pic,
               max_font_size=100,
               font_path="C:/Windows/Fonts/msyh.ttc",
               random_state=42,  # 为每个词返回一个PIL颜色
               )
positionAdvantage = data1.values[12]  # 职位诱惑
positionLables = data1.values[13]  # 标签
pa = positionAdvantage.tolist()
for t in range(0, len(pa)):
    pa[t] = str(pa[t])
pa_data = ",".join(pa)
pa_data = jieba.cut(pa_data)
pl = positionLables.tolist()
for t in range(0, len(pl)):
    pl[t] = str(pl[t])
pl_data = ",".join(pl)
pl_data = jieba.cut(pl_data)
pl_wd = []
pa_wd = []
spd = open("E:\\编程学习\\Project\\lagou\\stopword.txt", "r")
stopword = spd.read()
for pa_w in pa_data:
    if pa_w.strip() not in stopword:
        pa_wd.append(pa_w)
pa_wd = " ".join(pa_wd)
for pl_w in pl_data:
    if pl_w.strip() not in stopword:
        pl_wd.append(pl_w)
pl_wd = " ".join(pl_wd)
spd.close()
wc.generate(pl_wd)
pp.imshow(wc)
pp.axis('off')
# 绘制词云
pp.figure()
pp.axis('off')
# 保存图片
wc.to_file("E:\\编程学习\\Project\\lagou\\2.png")
