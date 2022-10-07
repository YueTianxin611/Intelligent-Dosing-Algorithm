#data_921 = pd.read_csv(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_921.csv')
import pandas as pd
import numpy as np

data1 = pd.read_csv('C:/Users/tianxinxin/Desktop/9.25/data_prepare_picture/result.csv')
data2 = pd.read_csv('C:/Users/tianxinxin/Desktop/9.25/1/result_921.csv')
columns = ['图像参数1',"图像参数2","图像参数3","图像参数4","图像参数5","图像参数6",
           "图像参数7","图像参数8","图像参数9","图像参数10","PH","温度","进水浊度",
           "电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）","智能加药池出水浊度"]
columns1 = ['图像参数1',"图像参数2","图像参数3","图像参数4","图像参数5","图像参数6",
           "图像参数7","图像参数8","图像参数9","图像参数10","PH","温度","进水浊度",
           "电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）","智能加药池出水浊度","结果出水浊度"]
columns2 = ['图像参数1',"图像参数2","图像参数3","图像参数4","图像参数5","图像参数6",
           "图像参数7","图像参数8","图像参数9","图像参数10","PH","温度","进水浊度",
           "电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）","智能加药池出水浊度","结果出水浊度"]
data1 = pd.DataFrame(data=data1,columns=columns1)
data2 = pd.DataFrame(data=data2,columns=columns2)

#data_out = pd.merge(data1,data2,on=['图像参数1',"图像参数2","图像参数3","图像参数4","图像参数5","图像参数6",
          # "图像参数7","图像参数8","图像参数9","图像参数10","PH","温度","进水浊度",
           #"电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）","智能加药池出水浊度"],right_index=True,how='outer')

#data_out = data_out.dropna(axis=0, how='any')

#data_out = data1.join(data2,on=['图像参数1',"图像参数2","图像参数3","图像参数4","图像参数5","图像参数6",
           #"图像参数7","图像参数8","图像参数9","图像参数10","PH","温度","进水浊度",
           #"电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）","智能加药池出水浊度"])


#data_out = pd.concat([data1,data2],axis=0)
#print(len(data_out))
#data_out.to_csv('C:/Users/tianxinxin/Desktop/9.25/1/result_all_divide_922.csv', encoding="utf_8_sig")
#data_out = pd.merge(data1,data2)
'''
data_out = pd.DataFrame(columns=["结果出水浊度","921结果出水浊度"])
list1 = [0]*2
list2 = []

for var in columns:
    for j in range(len(data2)):
        for i in range(len(data1)):
            if data2[var][j] == data1[var][i]:
                list1.append([data1["结果出水浊度"][j],data2["921结果出水浊度"][i]])
                #data_out = data_out.append(data1["结果出水浊度"][j],data2["921结果出水浊度"][i])

'''

data_out = pd.read_csv('C:/Users/tianxinxin/Desktop/9.25/1/result_all_divide_921.csv')
def ab(data):
    print(data)
    return data


data = data_out.groupby(['图像参数1', "图像参数2", "图像参数3", "图像参数4", "图像参数5", "图像参数6",
                     "图像参数7", "图像参数8", "图像参数9", "图像参数10", "PH", "温度", "进水浊度",
                     "电导率", "混凝剂投加量（mg/L）", "絮凝剂投加量（mg/L）","智能加药池出水浊度"])["结果出水浊度"].sum()
print(data)
data.to_csv('C:/Users/tianxinxin/Desktop/9.25/1/group921.csv', encoding="utf_8_sig")
#print(data_out)


