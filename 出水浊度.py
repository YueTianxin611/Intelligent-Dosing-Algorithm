import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
data1 = pd.read_excel('C:/Users/tianxinxin/Desktop/drug/data-0910-0903.xlsx')
tuxiang = data1["图像参数1"]
zhuodu = data1["出水水质定义"]

#fig = plt.figure()

T_1 = []
T_0 = []
for n in range(10155):
    if zhuodu[n] == 1:
        T_1.append(tuxiang[n])
    else:
        T_0.append(tuxiang[n])


#plt.subplot(221)
ax1=plt.subplot(2,1,1)
ax2=plt.subplot(212,sharey=ax1)
x1 = range(len(T_1))
x2 = range(len(T_0))
y1 = T_1
y2 = T_0
#ax1.scatter(x1, y1,color='red',marker='.')
ax1.hist(y1, bins= 20,color = 'steelblue',edgecolor = 'k')
#ax2.scatter(x2, y2,color='blue',marker='.')
ax2.hist(y2, bins= 20,color = '',edgecolor = 'k')
#plt.subylabel("图像参数1数值")
#plt.subxlabel("水质为1")
#ax2.ylabel("图像参数1数值")
#ax2.xlabel("水质为0")
plt.suptitle('picture_parameter1')
#plt.ylabel('parameter value')
plt.show()

from numpy import array
from numpy.random import normal, randint
from numpy import mean, median
from scipy.stats import mode
from numpy import mean, ptp, var, std
num = T_0
#print(mean(num))
#print(median(num))
#print(mode(num))
#print(ptp(num))
#print(std(num))

#print(mean(tuxiang))
#print(median(tuxiang))
#from numpy import array, cov, corrcoef
#data = array([tuxiang, zhuodu])
#cov(data, bias=1)
#print(corrcoef(data))
bins = 40
mu1 = np.mean(T_1)
sigma1 = np.std(T_1)
y1 = mlab.normpdf(bins, mu1, sigma1)
mu2 = np.mean(T_0)
sigma2 = np.std(T_0)
y2 = mlab.normpdf(bins, mu2, sigma2)
#plt.plot(bins, y1, 'b--')
#plt.plot(bins, y2, 'r--')
plt.hist(T_1,bins=40,label='water quality=1',color='steelblue',edgecolor = 'k',alpha=0.7)
plt.hist(T_0,bins=40,label='water quality=0',color='red',edgecolor = 'k',alpha=0.5)
plt.title('picture_parameter10')
plt.xlabel('parameter value')
#plt.ylabel('水质为1/0的数量')
plt.legend()
plt.show()
