# 误差描述
def des_error(data_error):
    print("标准查差是", data_error.std())
    print("误差差均值是", data_error.mean())
    print('----------------------------------------------------')
    data_error_abs = np.abs(data_error)
    print("最大误差", data_error_abs.max())
    print("平均误差", data_error_abs.mean())
    return None


# 分类准确率分数（指所有分类正确的百分比）
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_predict, y_test)

# 平均绝对误差
from sklearn.metrics import mean_absolute_error
error = mean_absolute_error(y_test, y_pred)


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


# 交叉验证
def cross_error(model):
    scores = cross_val_score(
             model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    return scores,scores.mean()


