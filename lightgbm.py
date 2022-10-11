# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.datasets import  make_classification
from sklearn.metrics import accuracy_score 
import matplotlib.pylab as plt
from sklearn import preprocessing

from sklearn.externals import joblib

def data_joint(data_list):
    data_all = pd.DataFrame(columns = data_list[0].columns)
    for i in data_list:
        data_all = data_all.append(i,ignore_index=True)
    return data_all

#数据准备 
f10 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_20\data_pre_910_.csv','rb')
data_10 = pd.read_csv(f10)
f11 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_20\data_pre_911_.csv','rb')
data_11 = pd.read_csv(f11)
f12 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_20\data_pre_912_.csv','rb')
data_12 = pd.read_csv(f12)
f13 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_20\data_pre_913_.csv','rb')
data_13 = pd.read_csv(f13)
f14 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_20\data_pre_914_.csv','rb')
data_14 = pd.read_csv(f14)
f15 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_20\data_pre_915_.csv','rb')
data_15 = pd.read_csv(f15)
f17 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_20\data_pre_917_.csv','rb')
data_17 = pd.read_csv(f17)
f18 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_20\data_pre_918_.csv','rb')
data_18 = pd.read_csv(f18)
f19 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_20\data_pre_919_.csv','rb')
data_19 = pd.read_csv(f19)

##数据准备 
#f10 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_910_40.csv','rb')
#data_10 = pd.read_csv(f10)
#f11 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_911_40.csv','rb')
#data_11 = pd.read_csv(f11)
#f12 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_912_40.csv','rb')
#data_12 = pd.read_csv(f12)
#f13 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_913_40.csv','rb')
#data_13 = pd.read_csv(f13)
#f14 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_914_40.csv','rb')
#data_14 = pd.read_csv(f14)
#f15 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_915_40.csv','rb')
#data_15 = pd.read_csv(f15)
#f17 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_917_40.csv','rb')
#data_17 = pd.read_csv(f17)
#f18 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_918_40.csv','rb')
#data_18 = pd.read_csv(f18)
#f19 = open(r'C:\Users\018614\Desktop\工作文件\智能加药\智能加压—修正版\data_lagging_40\data_pre_919_40.csv','rb')
#data_19 = pd.read_csv(f19)

data = data_joint([data_13,data_14,data_15,data_17,data_18])
#data['delta_混凝剂'] = data['delta_混凝剂']/2
#data['当前混凝剂投加量'] = data['当前混凝剂投加量']/2
data_in = data[['delta_混凝剂', 'delta_絮凝剂',"图像参数1","图像参数3","图像参数8",\
                "PH","温度","进水浊度","电导率",'当前混凝剂投加量','当前絮凝剂投加量','当前出水浊度','delta_出水浊度']]

# 加载数据
target = data_in['delta_出水浊度']
data_in = data_in.drop(['delta_出水浊度'],axis=1)

varss =list( data_in.columns)
target = np.array(target)
data = np.array(data_in)

X_train,X_test,y_train,y_test =train_test_split(data,target,test_size=0.3)

lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

param = {
    'max_depth':10,
    'num_leaves':18,
    'learning_rate':0.05,
    'scale_pos_weight':1,
    'num_threads':8,
    'objective':'regression',
    'bagging_fraction':0.9,
    'bagging_freq':1,
    'min_sum_hessian_in_leaf':0.001
}
param['is_unbalance']='true'
#param['metric'] = 'quantile'
param['metric'] = 'auc'
print('Start training...')

 
gbm = lgb.train(param,
                lgb_train,
                num_boost_round=500,
                valid_sets=lgb_eval,
                )

y_predict = gbm.predict(X_test)

# 误差描述
def des_error(data_error):
   
    print("标准查差是",data_error.std())
    print("误差差均值是",data_error.mean())
    print('----------------------------------------------------')
    data_error_abs = np.abs(data_error)
    print("最大误差",data_error_abs.max())
    print("平均误差",data_error_abs.mean())
    return None


ori_error = (y_predict - y_test)/(y_test+X_test[:,-1])
des_error(ori_error)


#保存model
#joblib.dump(gbm,'model_2.m')

data = data_19
data['delta_混凝剂'] = data['delta_混凝剂']/2
data['当前混凝剂投加量'] = data['当前混凝剂投加量']/2
data_in_test = data[['delta_混凝剂', 'delta_絮凝剂',"图像参数1","图像参数3","图像参数8",\
                "PH","温度","进水浊度","电导率",'当前混凝剂投加量','当前絮凝剂投加量','当前出水浊度','delta_出水浊度']]

# 加载数据
target_test = data_in_test['delta_出水浊度']
data_in_test = data_in_test.drop(['delta_出水浊度'],axis=1)

target_test = np.array(target_test)
data_in_test = np.array(data_in_test)

#载入模型
gbm = joblib.load('clf.m')
y_predict_test = gbm.predict(data_in_test)

ori_error = (y_predict_test - target_test)/(target_test+data_in_test[:,-1])
des_error(ori_error)


drop = abs(target_test/data_in_test[:,-1])
drop_list = abs(drop)>0.2
y_predict_test = y_predict_test[drop_list]
target_test = target_test[drop_list]

ori_error = (y_predict_test - target_test)/(target_test)
des_error(ori_error)

print(len(target_test))

for i in range(len(y_predict_test)):
    if y_predict_test[i]>0:
        y_predict_test[i]=1
    else:
        y_predict_test[i]=0
        
for i in range(len(target_test)):
    if target_test[i]>0:
        target_test[i]=1
    else:
        target_test[i]=0


accuracy_lgbm = accuracy_score(y_predict_test,target_test)
print(accuracy_lgbm)
