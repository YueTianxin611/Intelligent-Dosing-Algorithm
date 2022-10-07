import numpy as np
import pandas as pd

data_in = pd.read_csv('C:/Users/tianxinxin/Desktop/9.25/data_prepare_picture/data_fenlei.csv')
columns = ['图像参数1',"图像参数2","图像参数3","图像参数4","图像参数5","图像参数6",
           "图像参数7","图像参数8","图像参数9","图像参数10","PH","温度","进水浊度",
           "电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）","结果出水浊度"]
data_in = pd.DataFrame(data=data_in,columns=columns)
print(data_in)
def ab(data):
    return list(data.values)


data = data_in.groupby(['图像参数1',"图像参数2","图像参数3","图像参数4","图像参数5","图像参数6",
           "图像参数7","图像参数8","图像参数9","图像参数10","PH","温度","进水浊度",
           "电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"])["结果出水浊度"].apply(ab)

data.to_csv('C:/Users/tianxinxin/Desktop/9.25/data_prepare_picture/res.csv',encoding="utf_8_sig")
