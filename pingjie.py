import pandas as pd
def data_joint(data_list):
    data_all = pd.DataFrame(columns = data_list[0].columns)
    for i in data_list:
        data_all = data_all.append(i,ignore_index=True)
    return data_all

#data_10 = pd.read_csv('data_pre_910_.csv')
#data_11 = pd.read_csv('data_pre_911_.csv')
#data_12 = pd.read_csv('data_pre_912_.csv')
#data_13 = pd.read_csv('data_pre_913_.csv')
#data_14 = pd.read_csv('data_pre_914_.csv')
#data_15 = pd.read_csv('data_pre_915_.csv')
#data_17 = pd.read_csv('data_pre_917_.csv')
#data_18 = pd.read_csv('data_pre_918_.csv')
#data_19 = pd.read_csv('data_pre_919_.csv')

#数据准备
f9 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_909.csv','rb')
data_9 = pd.read_csv(f9)
data_9['混凝剂投加量（mg/L）'] = data_9['混凝剂投加量（mg/L）']/2
f10 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_910.csv','rb')
data_10 = pd.read_csv(f10)
data_10['混凝剂投加量（mg/L）'] = data_10['混凝剂投加量（mg/L）']/2
f11 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_911.csv','rb')
data_11 = pd.read_csv(f11)
data_11['混凝剂投加量（mg/L）'] = data_11['混凝剂投加量（mg/L）']/2
f12 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_912.csv','rb')
data_12 = pd.read_csv(f12)
data_12['混凝剂投加量（mg/L）'] = data_12['混凝剂投加量（mg/L）']/2
f13 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_913.csv','rb')
data_13 = pd.read_csv(f13)
data_13['混凝剂投加量（mg/L）'] = data_13['混凝剂投加量（mg/L）']/2
f14 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_914.csv','rb')
data_14 = pd.read_csv(f14)
data_14['混凝剂投加量（mg/L）'] = data_14['混凝剂投加量（mg/L）']/2
f15 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_915.csv','rb')
data_15 = pd.read_csv(f15)
data_15['混凝剂投加量（mg/L）'] = data_15['混凝剂投加量（mg/L）']/2
f17 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_917.csv','rb')
data_17 = pd.read_csv(f17)
data_17['混凝剂投加量（mg/L）'] = data_17['混凝剂投加量（mg/L）']/2
f18 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_918.csv','rb')
data_18 = pd.read_csv(f18)
data_18['混凝剂投加量（mg/L）'] = data_18['混凝剂投加量（mg/L）']/2
f19 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_919.csv','rb')
data_19 = pd.read_csv(f19)
data_19['混凝剂投加量（mg/L）'] = data_19['混凝剂投加量（mg/L）']/2
f20 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_920.csv','rb')
data_20 = pd.read_csv(f20)
data_20.loc[:11248,'混凝剂投加量（mg/L）'] = data_20.loc[:11248,'混凝剂投加量（mg/L）']/2
f21 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_921.csv','rb')
data_21 = pd.read_csv(f21)
f22 = open(r'C:\Users\tianxinxin\Desktop\9.25\data_prepare_picture\data_pre_922.csv','rb')
data_22 = pd.read_csv(f22)


#data = data_joint([data_10,data_11,data_12,data_13])
data = data_joint([data_9,data_10,data_11,data_12,data_13,data_14,data_15,data_17,data_18,data_19,data_20])

data = pd.DataFrame(data)
data.to_csv(r'C:\Users\tianxinxin\Desktop\9.25\1\data_pre_all.csv',encoding="utf_8_sig")
