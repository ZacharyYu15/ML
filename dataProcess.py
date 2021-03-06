#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


def norm(datasets,str):
    '''
    归一化数据
    Inputs:
    -datasets:数据集
    -str:要处理的数据特征
    '''
    sample_mean = datasets[str].mean()
    sample_std = datasets[str].std()
    datasets[str] = (datasets[str] - sample_mean)/sample_std
    


# In[ ]:


def getSeveralAtt(datasets,str,num):
    '''
    从数据中提取出ｎｕｍ个属性结点(等深提取)
    Inputs:
    -datasets:数据集
    -str:属性名称
    -num:要提取出来的个数
    
    Outputs:
    -att:从数据及中提取出的属性结点
    '''
    if num == None:
        att = list(set(datasets[str]))
        return att
    att = []
    dataList = list(datasets[str])
    dis = int(len(dataList)/num)
    dataList.sort()
    for i in range(num):
        att.append(dataList[i*dis - 1])
    att = list(set(att))
    return att


# In[ ]:


def transOnehot(dataSet,index):
    '''
    将数据转换成Onehot类型
    '''
    length = len(dataSet)
    max = dataSet[index].max().astype(int)
    result = []
    for number in dataSet[index]:
        zero = np.zeros(max + 1)
        zero[int(number)] = 1
        result.append(zero.tolist())
    return np.array(result)


# In[ ]:


#留出法
def hold_out(dataSet,train_size):
    """
    dataSet:数据集
    train_size:留出法中训练集所占得比例
    """
    totalLen = dataSet.shape[0]
    len = int(totalLen * train_size)
    index = range(totalLen)
    index_1 = np.random.choice(index,len,replace=False)     #训练集的下标
    index_2 = np.delete(index,index_1)                      #测试集的下标
    train = dataSet[index_1]
    test = dataSet[index_2]
    return train,test


# In[ ]:


#交叉验证法
def cross_valid(dataSet,k=10):
    """
    dataSet:数据集
    k：k次交叉验证的数目
    return : datasets：shape(k,num,feature)  list类型
    """
    datasets =[]
    num = int(dataSet.shape[0]/k)
    start = 0
    end = num
    for i in range(k):
        datasets.append(dataSet[start:end,:].tolist())
        start += num
        end += num
    return datasets


# In[ ]:


#自助法
def bootstrapping(dataSet):
    m = dataSet.shape[0]
    index1 = []
    index2 = []
    for i in range(m):
        index1.append(np.random.randint(m))
    index2 = np.delete(range(m),index1)
    train = dataSet[index1]
    test = dataSet[index2]
    return train,test


# In[ ]:




