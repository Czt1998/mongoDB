 # codeing utf-8

"""
created on:2018/06/07
author:Czt
target:获取时光网中电影的公司并存入mongoDB
finished on:2018/06/07
"""

import sys
import requests
import time
import re
import json
import urllib
import os
import urllib.request
from pymongo import MongoClient
from selenium import webdriver
from imp import reload
reload(sys)

driver = webdriver.PhantomJS(executable_path='/home/czt/PycharmProjects/phantomjs')
# conn = MongoClient('192.168.235.55', port=27017)
# db = conn['admin']
# db.authenticate("admin", "123456")
# db = conn['team_behind_sc']
# table = db['Film_company']
conn = MongoClient()
db = conn.mydb

def main():
#     years = [u'2010',u'2011']
#     for year in years:
#         year_0 = year
#         id = get_movie(year_0)
#         with open("/home/czt/PycharmProjects/untitled1/movie_name_" + year_0 + ".txt") as f:
#             lines = f.readlines()
#             for line in lines:
#                 time.sleep(1)
#                 movie_name = line.replace('\n', '')  # 因匹配的需要，将电影名的换行符去掉
#                 print(type(movie_name)),
#                 print(movie_name)
#                 pre_url = 'http://search.mtime.com/search/?q=' + urllib.request.quote(
#                     movie_name)  # 通过时光网url的特征，利用quoto将电影名拼接得到目标url
#                 print(pre_url)
#                 driver.get(pre_url)
#                 time.sleep(1)
#                 urls = driver.find_elements_by_xpath("//div[@class='main']/ul/li/h3/a")  # 利用xpath得到带有电影编号的链接
#                 time.sleep(1)
#                 print(urls)
#                 print(len(urls))
#                 if len(urls) == 0:
#                     with open('./movie_failed_' + year_0 + '.txt', "a+")as w:
#                         w.writelines("Fail in find" + movie_name)
#                         w.write('\n')
#                 all_urls = [i.get_attribute("href") for i in urls]
#                 time.sleep(1)
#                 count = 0
#                 for urls in all_urls:
#                     # 获得电影名与年份
#                     print(urls)
#                     driver.get(urls)
#                     name = driver.find_element_by_xpath("//div[@class='clearfix']/h1").text
#                     year = driver.find_element_by_xpath("//div[@class='clearfix']/p[@class='db_year']/a").text
#                     time.sleep(0.5)
#                     print(type(name)),
#                     print(name)
#                     print(type(year)),
#                     print(year)
#                     time.sleep(1)
#                     if name == movie_name and year == year_0:
#                         time.sleep(1)
#                         count = 1
#                         get_company(urls, movie_name, id[movie_name],year_0)
#                         time.sleep(1)
#                         break
#                     else:
#                         pass
#                 if count == 0:
#                     with open('./movie_failed_' + year_0 + '.txt', "a+")as w:
#                         w.writelines("Fail in name" + movie_name)
#                         w.write('\n')
#
#
# def get_movie(year_0):
#     """
#     获取电影id并切片出电影名
#     :return: id
#     """
#     id = {}
#     with open("/home/czt/PycharmProjects/untitled1/" + year_0 + ".txt", "r")as f:
#         fp = f.readlines()
#         for line in fp:
#             movie_n = line.split('')[0]
#             movie_id = line.split('')[1]
#             movie_id = movie_id.replace('\n', '')
#             id[movie_n] = movie_id
#             movie_name = line.split("")[0]
#             with open("/home/czt/PycharmProjects/untitled1/movie_name_" + year_0 + ".txt", "a+")as m:
#                 m.write(str(movie_name) + '\n')
#             print(movie_name)
#     return id
# def get_company(urls, movie_name,id,year_0):
#     """
#     获取制作公司与发行公司
#     :param urls: 电影公司信息链接
#     :param movie_name: 电影名
#     :param id: 电影id
#     :return: void
#     """
#     print("Successfully used")
#     w = requests.get(urls + "details.html#company")
#     w.encoding = 'utf-8'
#     html = w.text
#     # print(html)
#     p_company = 0
#     l_company = 0
#     res = {}
#     try:
#         data = re.findall('<div class="fl wp49">.*?</div>', html)[0]
#         all = re.findall('<a href="(.*?)".*?>(.*?)</a>', data)
#         zc = {}
#         for each in all:
#             company_name = each[1]
#             company_name = company_name.replace('.','')
#             zc[company_name] = each[0]
#         res['p_company'] = zc
#         p_company = 1
#     except:
#         #将存取失败的文件写入movie_fail文件
#         with open('./movie_failed_' + year_0 + '.txt',"a+")as w:
#             w.writelines("No p_company" + movie_name + id)
#             w.write('\n')
#
#     try:
#         data = re.findall('<div class="fl wp49">.*?</div>', html)[1]
#         all = re.findall('<a href="(.*?)".*?>(.*?)</a>', data)
#         pc = {}
#         for each in all:
#             company_name = each[1]
#             company_name = company_name.replace('.','')
#             pc[company_name] = each[0]
#         res['l_campany'] = pc
#         l_company = 1
#     except:
#         # 将存取失败的文件写入movie_fail文件
#         with open('./movie_failed_' + year_0 + '.txt', "a+")as w:
#             w.writelines("No l_company" + movie_name + id)
#             w.write('\n')
#
#     #print(flag)
#     #flag作为判断标志，当制作公司与发硬公司都存在时有效，此时flag为2
#
#     print("store" + '\n')
#     res = json.dumps(res)
#     s = json.loads(res)
#     mongoDB_insert(id, movie_name, s,p_company,l_company,year_0)
#
# def mongoDB_insert(id,movie_name,s,p_company,l_company,year_0):
#     """
#     将公司信息存入mongoDB
#     :param id: 电影id
#     :param movie_name: 电影名
#     :param s: 储存着公司信息的字典
#     :return: void
#     """
#     if l_company == 1 and p_company == 1:
#         db.col.insert({'_id': id, 'year': year_0,
#                        'movie_name': movie_name,
#                        'p_company': s['p_company'],
#                        'l_campany': s['l_campany']
#                        })
#     if l_company == 1 and p_company == 0:
#         db.col.insert({'_id': id, 'year': year_0,
#                        'movie_name': movie_name,
#                        'p_company': "null",
#                        'l_campany': s['l_campany']
#                        })
#     if l_company == 0 and p_company == 1:
#         db.col.insert({'_id': id, 'year': year_0,
#                        'movie_name': movie_name,
#                        'p_company': s['p_company'],
#                        'l_campany': "null"
#                        })
#     if l_company == 0 and p_company == 0:
#         db.col.insert({'_id': id, 'year': year_0,
#                        'movie_name': movie_name,
#                        'p_company': "null",
#                        'l_campany': "null"
#                        })

        # db.col.remove()
    for item in db.col.find().sort('id'):
        print(item)
        print('\n')

if __name__ == '__main__':
    main()
