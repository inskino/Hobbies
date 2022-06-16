# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:15:15 2022

@author: QICAI
"""

# !/usr/bin/env python
# coding: utf-8
import akshare as ak
 
import pandas as pd

# (jupyternotebook 画图用的，别的工具可以不用)
# %matplotlib auto
# 正常显示画图时出现的中文和负号
from pylab import mpl
import matplotlib.pyplot as plt
import seaborn as sns
 
 
 
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows',None)
 
 
# '''历史行情数据-通用'''
index_zh_a_hist_df = ak.index_zh_a_hist(symbol="000001", period="daily", start_date="19700101", end_date="22220101")
# print(index_zh_a_hist_df)
# print(index_zh_a_hist_df.values[:, [0, 2]])
# 设置为seaborn的样式，更美观
sns.set()
# 绘制收盘价曲线
index_zh_a_hist_df.plot(y="收盘")
index_zh_a_hist_df.index = pd.to_datetime(index_zh_a_hist_df['日期'])
# print(index_zh_a_hist_df.index[:5])
 
 
 
#
index_zh_a_hist_df = index_zh_a_hist_df.sort_index(ascending=True)
plt.figure(figsize=(12, 6))
index_zh_a_hist_df['收盘'].plot()
index_zh_a_hist_df['收盘'].rolling(60).mean().plot()
plt.show()
 
 
# '''股票指数信息一览表'''
# index_stock_info_df = ak.index_stock_info()
# print(index_stock_info_df.values)
# '''指数名称'''
# c = ak.index_value_name_funddb()
# print(c.values[:, 0])
# '''指数估值-韭圈儿choice of {'市盈率', '市净率', '股息率'}'''
# index_value_hist_funddb_df = ak.index_value_hist_funddb(symbol="上证指数", indicator="市盈率")
# print(index_value_hist_funddb_df)
 
 
# '''中国股票指数成份'''
# index_stock_cons_df = ak.index_stock_cons(symbol="000300")
# print(index_stock_cons_df)
# '''输出参数-按市场归类'''
# index_stock_cons_df = ak.index_stock_cons(symbol="000300")  # 主要调用 ak.stock_a_code_to_symbol() 来进行转换
# index_stock_cons_df['symbol'] = index_stock_cons_df['品种代码'].apply(ak.stock_a_code_to_symbol)
# print(index_stock_cons_df)
 
 
 
 
'''A 股等权重与中位数市盈率'''
# https://jishuin.proginn.com/p/763bfbd62d58
stock_a_ttm_lyr_df = ak.stock_a_ttm_lyr()
# print(stock_a_ttm_lyr_df.values[-1,1 :])
k = pd.to_numeric(stock_a_ttm_lyr_df.values[-1, 1:], downcast='integer')
# print(type(k))
i = []
for p in k:
    i.append(p)
print('全A股滚动市盈率(TTM)中位数', i[0], '\n全A股滚动市盈率(TTM)等权平均', i[1], '\n全A股静态市盈率(LYR)中位数', i[2],
      '\n全A股静态市盈率(LYR)等权平均', i[3], '\n当前"TTM(滚动市盈率)中位数"在历史数据上的分位数', i[4], '\n当前"TTM(滚动市盈率)中位数"在最近10年数据上的分位数', i[5],
      '\n当前"TTM(滚动市盈率)等权平均"在历史数据上的分位数', i[6], '\n当前"TTM(滚动市盈率)等权平均"在在最近10年数据上的分位数', i[7],
      '\n当前"LYR(静态市盈率)中位数"在历史数据上的分位数',
      i[8], '\n当前LYR(静态市盈率)中位数在最近10年数据上的分位数', i[9], '\n当前"LYR(静态市盈率)等权平均"在历史数据上的分位数', i[10],
      '\n当前"LYR(静态市盈率)等权平均"在最近10年数据上的分位数', i[11], '\n沪深300指数', i[12])
 
 
now = i[1]
print('当前市盈率：',now)
min_data=pd.to_numeric(stock_a_ttm_lyr_df.values[:, 1], downcast='integer')
min = min_data.min()
max=min_data.max()
print('历史最小市盈率：',min)
print('历史最大市盈率：',max)
ratio = (now - min) / now
print("越小越适合入场ratio: {0:.2f}%".format(ratio * 100))
# 一般来说，动态市盈率(TTM)等权平均的数值在30以下市场行情大概率被低估，此时我们进场收益会比明显，当该数值大于60市场大概率被高估，此时应当停止买入，考虑出手。
 
 
 
 
# '''A 股等权重与中位数市净率'''
# stock_a_all_pb_df = ak.stock_a_all_pb()
# print(stock_a_all_pb_df.values[-1, :])
# k2 = pd.to_numeric(stock_a_all_pb_df.values[-1, 1:], downcast='integer')
# i2 = []
# for p2 in k2:
#     i2.append(p2)
# print( '全部A股市净率中位数', i[0], '\n全部A股市净率等权平均', i[1], '\n上证指数', i[2], '\n当前市净率中位数在历史数据上的分位数', i[3],
#       '\n当前市净率中位数在最近10年数据上的分位数', i[4], '\n当前市净率等权平均在历史数据上的分位数', i[5], '\n当前市净率等权平均在最近10年数据上的分位数', i[6])