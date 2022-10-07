import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import  linear_model
from sklearn.preprocessing import  PolynomialFeatures
from sklearn.linear_model import LinearRegression
import seaborn as sns

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
data = pd.read_csv('C:/Users/tianxinxin/Desktop/today/data/data_0906_1.csv')

#sns.pairplot(df ,hue ='当前出水浊度')
#plt.show()
'''
color = sns.color_palette()
sns.set_style('darkgrid')
features_list = df.columns.values
feature_importance = rf.feature_importances
sorted_idx = np.argsort(feature_importance)
plt.figure(figsize=(5,7))
plt.barh(range(len(sorted_idx)), feature_importance[sorted_idx], align='center')
plt.yticks(range(len(sorted_idx)), features_list[sorted_idx])
plt.xlabel('Importance')
plt.title('Feature importances')
plt.draw()
plt.show()
'''
def corr_(df):
    print(df.corr())
    return
print(corr_(data))
def LR():

    return