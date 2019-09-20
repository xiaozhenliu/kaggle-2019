from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

class LWLR(object):
    
    def __init__(self,k):
        self.k = k
    
    def fit(self,X,y):
        self.X = X
        self.y = y
        return self
        
        
    def predict(X):
        result = []
        for example in X:
            prediction = _predict_single(example)
            result.append(prediction)
            
        return np.array(result)
        
    def _predict_single():
        # 1.算距离，写成向量
        # 2.距离转化成权重（也是向量）
        # 3.权重，X,y 输入 sklearn的LinearRegression
        # 4.预测
        pass