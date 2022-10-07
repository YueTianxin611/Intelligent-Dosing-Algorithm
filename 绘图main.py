import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import os
import math


# 创建文件夹
def mkdir(path):
    '''
    :param path: 创建路径(char)
    :return:创建是否成功(bool)
    '''
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        return False


# 按文件日期和给定间隔绘图
def huatu(date, interval):
    '''
    :param date: 数据日期(char)例："0907"
    :param interval: 取平均的间隔(int)
    :return: 每个参数与加药量的图像
    '''

    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    # 文件名格式data-0907.xlsx
    # 若为绝对路径则在此修改
    filename = r'data-' + date +r'.xlsx'

    # 创建文件夹
    # 若文件夹已存在，则会创建失败
    if mkdir('./'+date+'/') != True:
        raise Exception("Invalid path")

    # 读取数据
    excel = pd.read_excel(filename,usecols=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19])
    excel2 = pd.read_excel(filename,usecols=[0])
    title = ['图像参数1','图像参数2','图像参数3','图像参数4','图像参数5','图像参数6','图像参数7','图像参数8','图像参数9',
         '图像参数10','PH','温度','进水浊度','流量','电导率','混凝剂投加量','絮凝剂投加量','智能加药池出水浊度']
    excel = excel.values
    excel2 = excel2.values

    # 计算无缺失的数据长度
    for indexs in range(len(excel)):
        if True in np.isnan(list(excel[indexs])):
            length = indexs
            break
        else :
            length = indexs + 1

    x_axis,y_axis = [],[]
    for i in range(18):
        y_axis.append([])

    # 每隔intervel个数据就求和取平均,记录到list中
    for j in range(math.floor(length/interval)):
        temporarylist = excel[interval*j:interval*(j+1)]
        temporary = np.sum(temporarylist,axis=0)
        temporary = temporary/interval
        for k in range(18):
            y_axis[k].append(temporary[k])
        x_axis.append(excel2[j*interval][0])

    # 每张图片绘制,命名
    for i in range(17):
        str = title[i]+'.jpg'

        # 调整出图图片大小和清晰度
        fig = plt.figure(figsize=(30,20), dpi=150, facecolor="white")

        ax1 = fig.add_subplot(111)
        ax1.plot(x_axis, y_axis[i],label = title[i])
        ax1.set_ylabel(title[i])

        ax1.set_title(date+title[i]+'+'+title[-1])
        # 建立第二坐标轴
        ax2 = ax1.twinx()  # this is the important function
        ax2.plot(x_axis, y_axis[-1], 'r',label = title[-1])
        ax2.set_ylabel(title[-1]+'红色')
        ax2.set_xlabel('时间（每一百个数据的第一个值）')
        ax1.legend(loc=2)
        ax2.legend(loc=0)
        plt.savefig('./'+date+'/'+str,dpi = 150)
        plt.show()
    return 0

if __name__ == "__main__":
    huatu('0901',100)

