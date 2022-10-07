import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

data1 = pd.read_excel('C:/Users/tianxinxin/Desktop/drug/data-0910-0903.xlsx')
tuxiang = data1["图像参数10"]
zhuodu = data1["出水水质定义"]
T_1 = []
T_0 = []
T_1_guess = []
T_0_guess = []
for n in range(10155):
    if zhuodu[n] == 1:
        T_1.append(n)
    else:
        T_0.append(n)
average_1 =6.44535763411279
average_0 = 6.0798248444342
for k in range(len(tuxiang)):
    if abs(tuxiang[k] - average_1) <= abs(tuxiang[k] - average_0):
        T_1_guess.append(k)
    else:
        T_0_guess.append(k)

print(len(T_1_guess),len(T_1))
print(len(T_0_guess),len(T_0))