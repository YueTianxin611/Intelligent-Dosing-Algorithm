import pandas as pd

data = pd.read_csv('C:/Users/tianxinxin/Desktop/drug/data_1_910.csv')
columns = ['图像参数1',"图像参数2","图像参数3","图像参数4","图像参数5","图像参数6",
           "图像参数7","图像参数8","图像参数9","图像参数10","PH","温度","进水浊度","电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）","智能加药池出水浊度"]
data = data[columns]
# 提取自变量最大最小值
'''
        if dict1["图像参数2"][i]>=edge2[0] and dict1["图像参数2"][i]<edge2[1]and dict1["图像参数3"][i]>=edge3[0] and dict1["图像参数3"][i]<edge3[1]\
           and dict1["图像参数4"][i]>=edge4[0] and dict1["图像参数4"][i]<edge4[1] and dict1["图像参数5"][i]>=edge5[1] and dict1["图像参数5"][i]<edge5[2] \
           and dict1["图像参数6"][i] >= edge6[0] and dict1["图像参数6"][i] < edge6[1] and dict1["图像参数7"][i] >= edge7[0] and dict1["图像参数7"][i] < edge7[1] \
           and dict1["图像参数8"][i] >= edge8[0] and dict1["图像参数8"][i] < edge8[1] and dict1["图像参数9"][i] >= edge9[1] and dict1["图像参数9"][i] < edge9[2]\
           and dict1["图像参数10"][i] >= edge10[0] and dict1["图像参数10"][i] < edge10[1]
'''
max_min = pd.DataFrame(columns=columns,index=['max','min'])
for n in columns:
    max_min[n][0] = max(data[n])
    max_min[n][1] = min(data[n])
step = []
# 把每个参数分成n组
def function1(n):
    edge1 = []
    edge2 = []
    edge3 = []
    edge4 = []
    edge5 = []
    edge6 = []
    edge7 = []
    edge8 = []
    edge9 = []
    edge10 = []
    edge11 = []
    edge12 = []
    edge13 = []
    edge14 = []
    edge15 = []
    edge16 = []
    edge17 = []
    for i in range(17):
        step.append((max_min[columns[i]][0] - max_min[columns[i]][1]) / n)
    for k in range(n+1):
        edge1.append(max_min[columns[0]][1] + k * step[0])
        edge2.append(max_min[columns[1]][1] + k * step[1])
        edge3.append(max_min[columns[2]][1] + k * step[2])
        edge4.append(max_min[columns[3]][1] + k * step[3])
        edge5.append(max_min[columns[4]][1] + k * step[4])
        edge6.append(max_min[columns[5]][1] + k * step[5])
        edge7.append(max_min[columns[6]][1] + k * step[6])
        edge8.append(max_min[columns[7]][1] + k * step[7])
        edge9.append(max_min[columns[8]][1] + k * step[8])
        edge10.append(max_min[columns[9]][1] + k * step[9])
        edge11.append(max_min[columns[10]][1] + k * step[10])
        edge12.append(max_min[columns[11]][1] + k * step[11])
        edge13.append(max_min[columns[12]][1] + k * step[12])
        edge14.append(max_min[columns[13]][1] + k * step[13])
        edge15.append(max_min[columns[14]][1] + k * step[14])
        edge16.append(max_min[columns[15]][1] + k * step[15])
        edge17.append(max_min[columns[16]][1] + k * step[16])
    water_max = []
    #for n in range(10000):
        #water_max[n] = max(data['智能加药池出水浊度'][(data[columns[0]]>=edge1[0])&(data[columns[0]]<edge1[1])])
    dict1 = data[(data["图像参数1"]>=edge1[0])&(data["图像参数1"]<edge1[1])].reset_index()
    dict2 = data[(data["图像参数1"]>=edge1[1])&(data["图像参数1"]<edge1[2])].reset_index()
    dict3 = data[(data["图像参数1"]>=edge1[2])&(data["图像参数1"]<edge1[3])].reset_index()
    dict4 = data[(data["图像参数1"]>=edge1[3])&(data["图像参数1"]<edge1[4])].reset_index()
    dict5 = data[(data["图像参数1"]>=edge1[4])&(data["图像参数1"]<edge1[5])].reset_index()
    dict6 = data[(data["图像参数1"]>=edge1[5])&(data["图像参数1"]<edge1[6])].reset_index()
    dict7 = data[(data["图像参数1"]>=edge1[6])&(data["图像参数1"]<edge1[7])].reset_index()
    dict8 = data[(data["图像参数1"]>=edge1[7])&(data["图像参数1"]<edge1[8])].reset_index()
    dict9 = data[(data["图像参数1"]>=edge1[8])&(data["图像参数1"]<edge1[9])].reset_index()
    dict10 = data[(data["图像参数1"]>=edge1[9])&(data["图像参数1"]<edge1[10])].reset_index()
    num = 0
    for i in range(len(dict1)):
        if dict1["图像参数2"][i]>=edge2[1] and dict1["图像参数2"][i]<edge2[2]and dict1["图像参数3"][i]>=edge3[3] and dict1["图像参数3"][i]<edge3[4]\
               and dict1["图像参数4"][i]>=edge4[3] and dict1["图像参数4"][i]<edge4[4]:
            num = num+1
    #print(num)
    print(edge8)










    return edge1,edge2 ,edge3 ,edge4 ,edge5,edge6 ,edge7,edge8 ,edge9 , edge10,edge11,edge12 ,edge13,edge14,edge15,edge16,edge17
function1(10)
'''
function1(10)
edge1 = function1(10)[0]
edge2 = function1(10)[1]
edge3 = function1(10)[2]
edge4 = function1(10)[3]
edge5 = function1(10)[4]
edge6 = function1(10)[5]
edge7 = function1(10)[6]
edge8 = function1(10)[7]
edge9 = function1(10)[8]
edge10 = function1(10)[9]
edge11 = function1(10)[10]
edge12 = function1(10)[11]
edge13 = function1(10)[12]
edge14 = function1(10)[13]
edge15 = function1(10)[14]
edge16 = function1(10)[15]
edge17 = function1(10)[16]

for i in range(len(data)):
    for n in range(10):
        if data['图像参数1'][i]>=edge1[0] and data["图像参数1"][i]<edge1[1]:
            if data['图像参数2'][i]>=edge2[0] and data["图像参数2"][i]<edge2[1]:
                if data['图像参数3'][i]>=edge3[0] and data["图像参数3"][i]<edge3[1]:

                    if data['图像参数4'][i]>=edge4[0] and data["图像参数4"][i]<edge4[1]:
                        if data['图像参数5'][i] >= edge5[0] and data["图像参数5"][i] < edge5[1]:
                            if data['图像参数6'][i]>=edge6[0] and data["图像参数6"][i]<edge6[1]:
                                if data['图像参数7'][i]>=edge7[0] and data["图像参数7"][i]<edge7[1]:
                                    if data['图像参数8'][i]>=edge8[0] and data["图像参数8"][i]<edge8[1]:
                                        if data['图像参数9'][i] >= edge9[0] and data["图像参数9"][i] < edge3[9]:
                                            if data['图像参数10'][i]>=edge10[0] and data["图像参数10"][i]<edge3[10]:
                                                if data["PH"][i]>=edge11[0] and data["PH"][i]<edge11[1]:
                                                    if data["温度"][i]>=edge12[0] and data["温度"][i]<edge12[1]:
                                                        if data["进水浊度"][i]>=edge13[0] and data["进水浊度"][i]<edge13[1]:
                                                            if data["电导率"][i]>=edge14[0] and data["电导率"][i]<edge14[1]:
                                                                if data["混凝剂投加量（mg/L）"][i]>=edge15[0] and data["混凝剂投加量（mg/L）"][i]<edge15[1]:
                                                                    if data["絮凝剂投加量（mg/L）"][i]>=edge16[0] and data["絮凝剂投加量（mg/L）"][i]<edge16[1]:
                if data['图像参数3'][i]>=edge3[1] and data["图像参数3"][i]<edge3[2]:
                    if data['图像参数4'][i]>=edge4[0] and data["图像参数4"][i]<edge4[1]:
                    if data['图像参数4'][i]>=edge4[1] and data["图像参数4"][i]<edge4[2]:
                    if data['图像参数4'][i]>=edge4[2] and data["图像参数4"][i]<edge4[3]:
                    if data['图像参数4'][i]>=edge4[3] and data["图像参数4"][i]<edge4[4]:
                    if data['图像参数4'][i]>=edge4[4] and data["图像参数4"][i]<edge4[5]:
                    if data['图像参数4'][i]>=edge4[5] and data["图像参数4"][i]<edge4[6]:
                    if data['图像参数4'][i]>=edge4[6] and data["图像参数4"][i]<edge4[7]:
                    if data['图像参数4'][i]>=edge4[7] and data["图像参数4"][i]<edge4[8]:
                    if data['图像参数4'][i]>=edge4[8] and data["图像参数4"][i]<edge4[9]:
                    if data['图像参数4'][i]>=edge4[9] and data["图像参数4"][i]<edge4[10]:
                if data['图像参数3'][i]>=edge3[2] and data["图像参数3"][i]<edge3[3]:
                    if data['图像参数4'][i]>=edge4[0] and data["图像参数4"][i]<edge4[1]:
                    if data['图像参数4'][i]>=edge4[1] and data["图像参数4"][i]<edge4[2]:
                    if data['图像参数4'][i]>=edge4[2] and data["图像参数4"][i]<edge4[3]:
                    if data['图像参数4'][i]>=edge4[3] and data["图像参数4"][i]<edge4[4]:
                    if data['图像参数4'][i]>=edge4[4] and data["图像参数4"][i]<edge4[5]:
                    if data['图像参数4'][i]>=edge4[5] and data["图像参数4"][i]<edge4[6]:
                    if data['图像参数4'][i]>=edge4[6] and data["图像参数4"][i]<edge4[7]:
                    if data['图像参数4'][i]>=edge4[7] and data["图像参数4"][i]<edge4[8]:
                    if data['图像参数4'][i]>=edge4[8] and data["图像参数4"][i]<edge4[9]:
                    if data['图像参数4'][i]>=edge4[9] and data["图像参数4"][i]<edge4[10]:
                if data['图像参数3'][i]>=edge3[3] and data["图像参数3"][i]<edge3[4]:
                    if data['图像参数4'][i]>=edge4[0] and data["图像参数4"][i]<edge4[1]:
                    if data['图像参数4'][i]>=edge4[1] and data["图像参数4"][i]<edge4[2]:
                    if data['图像参数4'][i]>=edge4[2] and data["图像参数4"][i]<edge4[3]:
                    if data['图像参数4'][i]>=edge4[3] and data["图像参数4"][i]<edge4[4]:
                    if data['图像参数4'][i]>=edge4[4] and data["图像参数4"][i]<edge4[5]:
                    if data['图像参数4'][i]>=edge4[5] and data["图像参数4"][i]<edge4[6]:
                    if data['图像参数4'][i]>=edge4[6] and data["图像参数4"][i]<edge4[7]:
                    if data['图像参数4'][i]>=edge4[7] and data["图像参数4"][i]<edge4[8]:
                    if data['图像参数4'][i]>=edge4[8] and data["图像参数4"][i]<edge4[9]:
                    if data['图像参数4'][i]>=edge4[9] and data["图像参数4"][i]<edge4[10]:
                if data['图像参数3'][i]>=edge3[4] and data["图像参数3"][i]<edge3[5]:
                if data['图像参数3'][i]>=edge3[5] and data["图像参数3"][i]<edge3[6]:
                if data['图像参数3'][i]>=edge3[6] and data["图像参数3"][i]<edge3[7]:
                if data['图像参数3'][i]>=edge3[7] and data["图像参数3"][i]<edge3[8]:
                if data['图像参数3'][i]>=edge3[8] and data["图像参数3"][i]<edge3[9]:
                if data['图像参数3'][i]>=edge3[9] and data["图像参数3"][i]<edge3[10]:
            if data['图像参数2'][i] >= edge2[1] and data["图像参数2"][i] < edge2[2]:


            if data['图像参数2'][i] >= edge2[2] and data["图像参数2"][i] < edge2[3]:
            if data['图像参数2'][i] >= edge2[3] and data["图像参数2"][i] < edge2[4]:

            if data['图像参数2'][i] >= edge2[4] and data["图像参数2"][i] < edge2[5]:
            if data['图像参数2'][i] >= edge2[5] and data["图像参数2"][i] < edge2[6]:

            if data['图像参数2'][i] >= edge2[6] and data["图像参数2"][i] < edge2[7]:
            if data['图像参数2'][i] >= edge2[7] and data["图像参数2"][i] < edge2[8]:

            if data['图像参数2'][i] >= edge2[8] and data["图像参数2"][i] < edge2[9]:
            if data['图像参数2'][i] >= edge2[9] and data["图像参数2"][i] < edge2[10]:




        if data['图像参数1'][i] >= edge1[1] and data["图像参数1"][i] < edge1[2]:




        if data['图像参数1'][i] >= edge1[2] and data["图像参数1"][i] < edge1[3]:





        if data['图像参数1'][i] >= edge1[3] and data["图像参数1"][i] < edge1[4]:






        if data['图像参数1'][i] >= edge1[4] and data["图像参数1"][i] < edge1[5]:





        if data['图像参数1'][i] >= edge1[5] and data["图像参数1"][i] < edge1[6]:






        if data['图像参数1'][i] >= edge1[6] and data["图像参数1"][i] < edge1[7]:

        if data['图像参数1'][i] >= edge1[7] and data["图像参数1"][i] < edge1[8]:
        if data['图像参数1'][i] >= edge1[8] and data["图像参数1"][i] < edge1[9]:
        if data['图像参数1'][i] >= edge1[9] and data["图像参数1"][i] < edge1[10]:
'''