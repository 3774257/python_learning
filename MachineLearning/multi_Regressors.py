from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import sklearn.svm as svm
from sklearn.neighbors import KNeighborsRegressor
from sklearn import ensemble


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def loaddata(n, regenerate=False):
    FILENAMENPY = '.\data\multi_regressors.npy'

    def recreatedata(n, filename):
        X = np.random.rand(n) * 15
        y = 0.5 * np.sin(X) + 0.1 * X + 3 + np.random.rand(n) * 0.2
        data = np.vstack((X, y))
        data = data.T
        # data[:][1] =
        # pickle.dump(data, '.\data\multi_regressors.pkldump')
        np.savetxt('.\data\multi_regressors.txt', data)
        np.save(filename, data)
        return data

    if not recreate or not os.path.exists(FILENAMENPY):
        try:
            data = np.load(FILENAMENPY)
        except FileNotFoundError:
            data = recreatedata(n, FILENAMENPY)
    else:
        data = recreatedata(n, FILENAMENPY)

    return data[:, 0].reshape((-1, 1)), data[:, 1]


def showdata(X_train, y_train, X_test, y_test):
    # 原始数据
    plt.figure()
    plt.scatter(X_train, y_train, marker='.', c='green', label='训练数据')
    plt.scatter(X_test, y_test, marker='.', c='red', label='测试数据')
    plt.title("原始数据划分")
    plt.legend()
    plt.show()


def linemode(X_train, y_train, X_test, XX_test, y_test):
    # 线性模型
    print("线性模型回归开始：")
    X_train_mp = X_train
    X_test_mp = X_test
    errors = []
    # plt.scatter(XX_train, y_train, marker='.', c='green')
    plt.figure(figsize=(8, 6))
    plt.scatter(XX_test, y_test, marker='.', c='blue')
    for i in range(1, 21, 3):
        if i > 1:
            X_train_mp = np.hstack((X_train_mp, X_train ** i))
            X_test_mp = np.hstack((X_test_mp, X_test ** i))
        reg = LinearRegression(n_jobs=3)
        reg.fit(X_train_mp, y_train)
        y_pred = reg.predict(X_test_mp)
        errors.append([i, mean_squared_error(y_test, y_pred)])
        print("线性模型", i, "次项 Coefficients", reg.intercept_, reg.coef_)
        mse = mean_squared_error(y_test, y_pred)
        print("线性模型 %d 次 Valid score: %.4f MSE: %.4f " % (i, reg.score(X_test_mp, y_test), mse))
        plt.plot(XX_test, y_pred, label="%d次 %.4f" % (i, mse))
    plt.title("N 次多项式模型")
    plt.legend()
    plt.show()

    # errors = np.array(errors)
    # plt.figure()
    # plt.plot(errors[:, 0], errors[:,1], 'o-')
    # plt.title("N 次线性模型均方差")
    # plt.show()
    # print("N 次线性模型均方差均方差 :", errors)


def createmodels():
    models = []
    modname = 'DTR'
    model = DecisionTreeRegressor
    params = {'max_depth': range(2, 13, 2)}
    models.append([modname, model, params])

    modname = 'SVR'
    model = svm.SVR
    params = {'kernel': ['linear', 'rbf']}
    models.append([modname, model, params])

    modname = 'KNN'
    model = KNeighborsRegressor
    params = {'n_neighbors': range(2, 12, 3)}
    models.append([modname, model, params])

    modname = 'RF'
    model = ensemble.RandomForestRegressor
    params = {'n_estimators': (10, 20, 50, 80, 100)}
    models.append([modname, model, params])

    modname = 'ADAboost'
    model = ensemble.AdaBoostRegressor
    params = {'n_estimators': (20, 50, 80, 100)}
    models.append([modname, model, params])

    modname = 'GBRT'
    model = ensemble.GradientBoostingRegressor
    params = {'n_estimators': (20, 50, 80, 100)}
    models.append([modname, model, params])

    return models


def main():
    n = 500
    X, y = loaddata(n, regenerate=False)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
    XX_train, XX_test = X_train.reshape((-1, 1)), X_test.reshape((-1, 1))
    y_test = y_test.reshape((-1, 1))
    test_data = np.hstack((XX_test, y_test))
    test_data = np.array(sorted(test_data, key=lambda x:x[0]))
    XX_test = test_data[:, 0].reshape((-1, 1))
    X_test = test_data[:, 0].reshape((-1, 1))
    y_test = test_data[:, 1].reshape((-1))

    showdata(X_train, y_train, X_test, y_test)
    linemode(X_train, y_train, X_test, XX_test, y_test)

    models = createmodels()

    for modname, model, params in models:
        print("%s 模型回归开始：" % modname)
        plt.figure(figsize=(8, 6))
        plt.scatter(XX_test, y_test, marker='.', c='blue')
        key = [k for k in params.keys()][0]
        for i in params[key]:
            tmppara = {key: i}
            dcr = model(**tmppara)
            dcr.fit(X_train, y_train)
            y_pred = dcr.predict(X_test)
            error_squared = mean_squared_error(y_test, y_pred)
            print("%s %s %s Valid score: %.4f, MSE: %.4f " %
                  (modname, key, i, dcr.score(X_test, y_test), error_squared))
            plt.plot(XX_test, y_pred, label='%s=%s MSE: %.4f' % (key, i, error_squared))
        plt.title("%s 回归" % modname)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    main()
