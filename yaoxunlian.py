import pandas as pd
import numpy as np
import lightgbm as lgb
import copy
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.datasets import  make_classification
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

data1 = pd.read_excel('C:/Users/tianxinxin/Desktop/drug/data_0902.xlsx',)
data2 = pd.read_excel('C:/Users/tianxinxin/Desktop/drug/data-0910-0903.xlsx',)
accuracy = []
for n in range(0,8):
    X_train = data1.loc[10000:10000+n*2500,["PH","温度","进水浊度","流量","电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"]]
    y_train = data1.loc[10000:10000+n*2500, "记录定义"]
    X_test = data1.loc[10000+n*2500:10000+(n+1)*2500, ["PH", "温度", "进水浊度", "流量", "电导率", "混凝剂投加量（mg/L）", "絮凝剂投加量（mg/L）"]]
    y_test = data1.loc[10000+n*2500:10000+(n+1)*2500, "记录定义"]

    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

    param = {
        'max_depth': 8,
        'num_leaves': 16,
        'learning_rate': 0.2,
        'scale_pos_weight': 1,
        'num_threads': 8,
        'objective': 'binary',
        'bagging_fraction': 1,
        'bagging_freq': 1,
        'min_sum_hessian_in_leaf': 0.001
    }
    # param['is_unbalance']='true'
    param['metric'] = 'auc'

    print('Start training...')

    gbm = lgb.train(param,
                    lgb_train,
                    num_boost_round=500,
                    valid_sets=lgb_eval,
                    )

    print('Start predicting...')

    y_predict_test = gbm.predict(X_test)

    for i in range(len(y_predict_test)):
        if y_predict_test[i] > 0.5:
            y_predict_test[i] = 1
        else:
            y_predict_test[i] = 0

    accuracy_lgbm = accuracy_score(y_predict_test, y_test)
    #print(accuracy_lgbm)
    accuracy.append(accuracy_lgbm)
    target_names = ['0', '1']
    #print(classification_report(y_test, y_predict_test,
                                #target_names=target_names))


print(accuracy)