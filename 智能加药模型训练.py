# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:09:54 2019

@author: 018614
"""

import pandas as pd
import numpy as np
import lightgbm as lgb
import copy
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.datasets import  make_classification
from sklearn.metrics import accuracy_score 
data1 = pd.read_excel('C:/Users/tianxinxin/Desktop/drug/data_0902.xlsx',)
data2 = pd.read_excel('C:/Users/tianxinxin/Desktop/drug/data-0910-0903.xlsx',)
#data_in = data1.iloc[:34162,1:11]#包含三个实验变量，及十个图像变量
#data_in = data1.loc[:34162,["图像参数1","图像参数2","图像参数3","图像参数4","图像参数5","图像参数6","图像参数7","图像参数8","图像参数9","图像参数10",\
#                            "混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"]]
#data_in = data1.loc[:34162,["PH","温度","进水浊度","流量","电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"]]
#target = data1.loc[:34162,"记录定义"] 
#varss =list( data_in.columns)
#target = np.array(target)
#data = np.array(data_in)

#X_train,X_test,y_train,y_test =train_test_split(data,target,test_size=0.4)
X_train = data1.loc[0:10000,["PH","温度","进水浊度","流量","电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"]]
X_test = data1.loc[15000:17500,["PH","温度","进水浊度","流量","电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"]]
y_train = data1.loc[0:10000,"记录定义"]
y_test = data1.loc[15000:17500,"记录定义"]


# create dataset for lightgbm
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

param = {
    'max_depth':8,
    'num_leaves':16,
    'learning_rate':0.2,
    'scale_pos_weight':1,
    'num_threads':8,
    'objective':'binary',
    'bagging_fraction':1,
    'bagging_freq':1,
    'min_sum_hessian_in_leaf':0.001
}
#param['is_unbalance']='true'
param['metric'] = 'auc'

print('Start training...')
 
gbm = lgb.train(param,
                lgb_train,
                num_boost_round=500,
                valid_sets=lgb_eval,
                )
 
print('Start predicting...')
 
y_predict_test = gbm.predict(X_test)
#print(y_predict_test)

for i in range(len(y_predict_test)):
    if y_predict_test[i]>0.5:
        y_predict_test[i]=1
    else:
        y_predict_test[i]=0


accuracy_lgbm = accuracy_score(y_predict_test,y_test)
print(accuracy_lgbm)
#geshu

def all_np(arr):
    """获取每个元素的出现次数，使用Numpy"""
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result
print(all_np(y_train))
print(all_np(y_test))

##保存模型
#from sklearn.externals import joblib
##使用sklearn中的模块joblib
#joblib.dump(gbm, 'gbm20190902a.pkl')

##特征选择
#df = pd.DataFrame(data_in.columns.tolist(), columns=['feature'])
#df['importance']=list(gbm.feature_importance())
#df = df.sort_values(by='importance',ascending=False)

from sklearn.metrics import classification_report
target_names = ['0','1']
print(classification_report(y_test, y_predict_test,
                            target_names=target_names))


