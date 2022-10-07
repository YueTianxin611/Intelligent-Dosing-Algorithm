import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV, RepeatedKFold, cross_val_score,cross_val_predict,KFold
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression  #线性回归
from sklearn import metrics
from sklearn.metrics import accuracy_score
data0 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0906.csv')
data1 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0907.csv')
data2 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0908.csv')
data3 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0909.csv')
data4 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0910.csv')
data5 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0911.csv')
data6 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0912.csv')
data7 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0913.csv')
data8 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0914.csv')
data9 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0915.csv')
data10 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0917.csv')
data11 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0918.csv')
data12 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0919.csv')
data13 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0920.csv')
data14 = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0921.csv')
def data_joint(data_list):
    data_all = pd.DataFrame(columns = data_list[0].columns)
    for i in data_list:
        data_all = data_all.append(i,ignore_index=True)
    return data_all

#data_all_1 = data_joint([data8])
#data_all_2 = data_joint([data5])
#data_all_1 = data_joint([data4])
#data_all_2 = data_joint([data5])
#data_all_1 = data_joint([data13])
#data_all_2 = data_joint([data14])
data_all_1 = data_joint([data5,data6,data7,data8,data9])
data_all_2 = data_joint([data10,data11,data12,data13,data14])
#data_all_1 = data_joint([data0,data1,data2,data3,data4])
#data_all_2 = data_joint([data5,data6,data7,data8,data9])
#data_all_1 = data_joint([data5,data6,data7,data8,data9])
#data_all_2 = data_joint([data10,data11])
#data_all_1 = data_joint([data8,data9,data10,data11,data12])
#data_all_2 = data_joint([data13,data14])
X_train = data_all_1[["图像参数1","图像参数2","图像参数3","图像参数4","图像参数5","图像参数6","图像参数7","图像参数8","图像参数9","图像参数10","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）","当前出水浊度"]]
y_train = data_all_1['智能加药池出水浊度']
X_test = data_all_2[["图像参数1","图像参数2","图像参数3","图像参数4","图像参数5","图像参数6","图像参数7","图像参数8","图像参数9","图像参数10","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）","当前出水浊度"]]
y_test = data_all_2['智能加药池出水浊度']
#print(X_train)
#mod = LinearRegression()
#model = mod.fit(X_train, y_train)
#print(mod.coef_)

#from sklearn import tree
#mod = tree.DecisionTreeRegressor()
#from sklearn import ensemble
#mod = ensemble.RandomForestRegressor(n_estimators=20)
from sklearn import ensemble
mod= ensemble.AdaBoostRegressor(n_estimators=50)


model = mod.fit(X_train, y_train)



y_pred = mod.predict(X_test)
#accuracy = accuracy_score(y_test,y_pred)
def m(model):
    scores = cross_val_score(
             model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    np.set_printoptions(precision=6,suppress=True)
    print(model.feature_importances_)
    return scores,scores.mean()
#m(model)
from sklearn.metrics import mean_absolute_error
error = mean_absolute_error(y_test, y_pred)
np.set_printoptions(precision=6,suppress=True)
print(model.feature_importances_)
print(error)


def des_error(data_error):
    print("标准查差是", data_error.std())
    print("误差差均值是", data_error.mean())
    print('----------------------------------------------------')
    data_error_abs = np.abs(data_error)
    print("最大误差", data_error_abs.max())
    print("平均误差", data_error_abs.mean())
    return None


# 误差图
def draw_error(data_error, fig):
    plt.figure(2 * fig)
    plt.hist(data_error, bins=500)
    plt.xlabel("origin Error")
    _ = plt.ylabel("Count")

    plt.figure(2 * fig + 1)
    data_error_abs = np.abs(data_error)
    plt.hist(data_error_abs, bins=500)
    plt.xlabel("origin Error")
    _ = plt.ylabel("Count")
    plt.show()
    return None

