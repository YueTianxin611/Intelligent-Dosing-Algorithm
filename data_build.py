# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 08:45:35 2019

@author: 018614
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:48:44 2019

@author: 018614
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:29:26 2019

@author: 018614
"""

import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt
import lightgbm as lgb
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import minmax_scale
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

data5 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0905.xlsx')
data6 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0906.xlsx')
data7 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0907.xlsx')
data8 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0908.xlsx')
data9 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0909.xlsx')
data10 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0910.xlsx')
data11 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0911.xlsx')
data12 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0912.xlsx')
data13 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0913.xlsx')
data14 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0914.xlsx')
data15 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0915.xlsx')
data17 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0917.xlsx')
data18 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0918.xlsx')
data19 = pd.read_excel(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data\data-0919.xlsx')



data_905 = data5.dropna(axis=0, how='any')
data_906 = data6.dropna(axis=0, how='any')
data_907 = data7.dropna(axis=0, how='any')
data_908 = data8.dropna(axis=0, how='any')
data_909 = data9.dropna(axis=0, how='any')
data_910 = data10.dropna(axis=0, how='any')
data_911 = data11.dropna(axis=0, how='any')
data_912 = data12.dropna(axis=0, how='any')
data_913 = data13.dropna(axis=0, how='any')
data_914 = data14.dropna(axis=0, how='any')
data_915 = data15.dropna(axis=0, how='any')
data_917 = data17.dropna(axis=0, how='any')
data_918 = data18.dropna(axis=0, how='any')
data_919 = data19.dropna(axis=0, how='any')

#构造样本集
def bulid_data_1(data):
    current = data['流量']
    data_1 = data.loc[:,["图像参数1","图像参数2","图像参数3","图像参数4","图像参数5","图像参数6","图像参数7","图像参数8","图像参数9","图像参数10",\
                                    "PH","温度","进水浊度","电导率",'混凝剂投加量（mg/L）','絮凝剂投加量（mg/L）','智能加药池出水浊度']]
    return current,data_1

#current_905,data_1_905 = bulid_data_1(data_905)

#平滑
def average_all(data,time):
    time = int(time*20)
    var_list = data.columns
    average_all_ = pd.DataFrame(columns = var_list)
    for i in var_list:
        test_data_1 = data[i]
        average = []
        for j in range(time,len(test_data_1)):
            temp = test_data_1[j-time+1:j].mean()
            average.append(temp)
        average_all_[i] = average
    return average_all_
#current_911,data_1_911 = bulid_data_1(data_911)
#average_all_905 = average_all(data_1_905,20)  
    
#在经过平滑处理的数据中将智能加药池出水浊度,两个加药量置前20*time阶
#def lagging(data,time): 
#    target_1 = data[['智能加药池出水浊度']][int(time*20)*2:].reset_index(drop = True)
#    target_2 = data[['混凝剂投加量（mg/L）','絮凝剂投加量（mg/L）']][:-int(time*20)*2].reset_index(drop = True)
#    data_var = data.iloc[int(time*20):-int(time*20),:].reset_index(drop = True)
#    data_var.rename(columns={'混凝剂投加量（mg/L）':'当前混凝剂投加量','絮凝剂投加量（mg/L）':'当前絮凝剂投加量','智能加药池出水浊度':'当前出水浊度'}, inplace = True)
#    lagging_ = pd.concat([data_var,target_1,target_2],axis=1)
#    return lagging_

def lagging(data,time): 
    target = data[['混凝剂投加量（mg/L）','絮凝剂投加量（mg/L）','智能加药池出水浊度']][int(time*20):].reset_index(drop = True)
    data_var = data.iloc[:-int(time*20),:].reset_index(drop = True)
    data_var.rename(columns={'混凝剂投加量（mg/L）':'当前混凝剂投加量','絮凝剂投加量（mg/L）':'当前絮凝剂投加量','智能加药池出水浊度':'当前出水浊度'}, inplace = True)
    lagging_ = pd.concat([data_var,target],axis=1)
    return lagging_


#lagging_905 = lagging(average_all_905,20)

def delta_lagging(data):
    data['delta_混凝剂'] = data['混凝剂投加量（mg/L）']-data['当前混凝剂投加量']
    data['delta_絮凝剂'] = data['絮凝剂投加量（mg/L）']-data['当前絮凝剂投加量']
    data['delta_出水浊度'] = data['智能加药池出水浊度']-data['当前出水浊度']
    data = data.drop(['智能加药池出水浊度','混凝剂投加量（mg/L）','絮凝剂投加量（mg/L）'],axis=1)
    return data

#data_pre_905 = delta_lagging(lagging_905)














def data_prepare(data,time):
    #不删除不稳定数据
    current,data_1 = bulid_data_1(data)
    average_all_ = average_all(data_1,time)  
    lagging_ = lagging(average_all_,time)
    data_pre_ = delta_lagging(lagging_)
    return data_pre_


time = 40
data_pre_905 = data_prepare(data_905,time)
data_pre_906 = data_prepare(data_906,time)
data_pre_907 = data_prepare(data_907,time)
data_pre_908 = data_prepare(data_908,time)
data_pre_909 = data_prepare(data_909,time)
data_pre_910 = data_prepare(data_910,time)
data_pre_911 = data_prepare(data_911,time)
data_pre_912 = data_prepare(data_912,time)
data_pre_913 = data_prepare(data_913,time)
data_pre_914 = data_prepare(data_914,time)
data_pre_915 = data_prepare(data_915,time)
data_pre_917 = data_prepare(data_917,time)
data_pre_918 = data_prepare(data_918,time)
data_pre_919 = data_prepare(data_919,time)


data_pre_905.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_905_40.csv')
data_pre_906.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_906_40.csv')
data_pre_907.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_907_40.csv')
data_pre_908.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_908_40.csv')
data_pre_909.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_909_40.csv')
data_pre_910.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_910_40.csv')
data_pre_911.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_911_40.csv')
data_pre_912.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_912_40.csv')
data_pre_913.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_913_40.csv')
data_pre_914.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_914_40.csv')
data_pre_915.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_915_40.csv')
data_pre_917.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_917_40.csv')
data_pre_918.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_918_40.csv')
data_pre_919.to_csv(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_919_40.csv')