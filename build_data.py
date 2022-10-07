import pandas as pd


data6 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0920.xls')
data_906 = data6.dropna(axis=0, how='any')
for i in range(len(data_906)):
    if i<= 9602:
        data_906.loc[i,'混凝剂投加量（mg/L）'] = data_906['混凝剂投加量（mg/L）'][i]/2
'''
data5 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0905.xlsx')
data6 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0906.xlsx')
data7 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0907.xlsx')
data8 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0908.xlsx')
data9 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0909.xlsx')
data10 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0910.xlsx')
data11 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0911.xlsx')
data12 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0912.xlsx')
data13 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0913.xlsx')
data14 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0914.xlsx')
data15 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0915.xlsx')
data17 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0917.xlsx')
data18 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0918.xlsx')
data19 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0919.xlsx')
data20 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0920.xls')
data21 = pd.read_excel('C:/Users/tianxinxin/Desktop/today/data-0921.xls')

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
data_920 = data20.dropna(axis=0, how='any')
data_921 = data21.dropna(axis=0, how='any')
'''
# 构造样本集
def build_data_1(data):
    current = data['流量']
    data_1 = data.loc[:,["图像参数1","图像参数2","图像参数3","图像参数4","图像参数5","图像参数6","图像参数7","图像参数8","图像参数9","图像参数10", \
                         '流量', '智能加药池出水浊度',"混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"]]
    return current,data_1
current,data_1=build_data_1(data_906)

# 平滑
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
av = average_all(data_1,5)

def lagging(data):
    data_values = pd.DataFrame(
        columns=["图像参数1", "图像参数2", "图像参数3", "图像参数4", "图像参数5", "图像参数6", "图像参数7", "图像参数8", "图像参数9", "图像参数10",
                 "智能加药池出水浊度","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"])
    for i in range(len(data)):
        index_2 = int(411.68*20*60/data['流量'][i]+i+1)
        if index_2<=len(data):
            values = data.iloc[index_2:index_2+1]
            data_values=data_values.append(values)
        else:
            pass
    data_values.rename(columns={'智能加药池出水浊度': '当前出水浊度'}, inplace=True)
    data_values = data_values.reset_index(drop=True)
    data_values = data_values.drop(['流量'],axis=1)
    target = data[['智能加药池出水浊度']][:len(data_values)].reset_index(drop=True)
    lagging_ = pd.concat([data_values, target], axis=1)
    return lagging_


def data_prepare(data):
    #不删除不稳定数据
    current,data_1 = build_data_1(data)
    average_all_ = average_all(data_1,5)
    data_pre_ = lagging(average_all_)
    return data_pre_


data_pre_906 = data_prepare(data_906)
#print(data_pre_905)
data_pre_906.to_csv('C:/Users/tianxinxin/Desktop/today/data/2/data_0920_try.csv',encoding="utf_8_sig")
'''
data_pre_905 = data_prepare(data_905)
data_pre_906 = data_prepare(data_906)
data_pre_907 = data_prepare(data_907)
data_pre_908 = data_prepare(data_908)
data_pre_909 = data_prepare(data_909)
data_pre_910 = data_prepare(data_910)
data_pre_911 = data_prepare(data_911)
data_pre_912 = data_prepare(data_912)
data_pre_913 = data_prepare(data_913)
data_pre_914 = data_prepare(data_914)
data_pre_915 = data_prepare(data_915)
data_pre_917 = data_prepare(data_917)
data_pre_918 = data_prepare(data_918)
data_pre_919 = data_prepare(data_919)
data_pre_920 = data_prepare(data_920)
data_pre_921 = data_prepare(data_921)


data_pre_905.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0905.csv',encoding="utf_8_sig")
data_pre_906.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0906.csv',encoding="utf_8_sig")
data_pre_907.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0907.csv',encoding="utf_8_sig")
data_pre_908.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0908.csv',encoding="utf_8_sig")
data_pre_909.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0909.csv',encoding="utf_8_sig")
data_pre_910.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0910.csv',encoding="utf_8_sig")
data_pre_911.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0911.csv',encoding="utf_8_sig")
data_pre_912.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0912.csv',encoding="utf_8_sig")
data_pre_913.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0913.csv',encoding="utf_8_sig")
data_pre_914.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0914.csv',encoding="utf_8_sig")
data_pre_915.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0915.csv',encoding="utf_8_sig")
data_pre_917.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0917.csv',encoding="utf_8_sig")
data_pre_918.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0918.csv',encoding="utf_8_sig")
data_pre_919.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0919.csv',encoding="utf_8_sig")
data_pre_920.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0920.csv',encoding="utf_8_sig")
data_pre_921.to_csv('C:/Users/tianxinxin/Desktop/today/data/data_0921.csv',encoding="utf_8_sig")
'''

