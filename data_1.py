#!/usr/bin/python
#-*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt          #导入matplotlib包
import numpy as np                       #导入numpy包
import time                              

def loadData():                           #读入文件
    f=open('ex1data1.txt')                      
    data = f.readlines()                  #一次读入文件     
    l=len(data)                           
    mat=zeros((l,2))                      #l*2的矩阵，初始化0       
    index=0                               
    xdata = ones((l,2))                   #l*2的矩阵，初始化为1
    ydata = []                       
    for line in data:
        line = line.strip()               #取出多余字符，    
        linedata = line.split(',')        #分割数据
        mat[index, :] = linedata[0:2]     #暂存在mat矩阵中
        index +=1
    xdata[:,1] = mat[:,0]                 #将mat的第0列存入xdata的第一列
    ydata = mat[:,1]                      #将mat的第1列存入ydata中
    return xdata,ydata

def model(theta,x):                       #直线方程
    theta = np.array(theta)
    return x.dot(theta)                   #返回直线的y值

def cost(theta,xdata,ydata,l):            #代价函数
    SUM = 0
    idex = 0
    ydata = mat (ydata)
    ydata = ydata.T
    for line in ydata:
          yp = model(theta,xdata[idex ,:]) 
          yp = yp - ydata[idex ,:]
          yp = yp**2
          SUM = SUM + yp
          idex  =idex +1
    return SUM/2/l                       #返回耗费

def grad(theta,idex1,xdata,ydata,sigmal,l):  #梯度计算
    idex = 0
    SUM = 0
    for line in ydata:
            yp = model(theta,xdata[idex ,:]) - ydata[idex] #计算梯度
            yp =yp * xdata[idex][idex1]
            idex  =idex +1
            SUM = SUM + yp
    return SUM/l


def gradlient(theta,xdata,ydata,sigmal,l):  #参数更新
    idex1 = 0
    for line1 in theta:
            theta[idex1] = theta[idex1] - sigmal * grad(theta,idex1,xdata,ydata,sigmal,l) #更新参数
            theta[idex1] = theta[idex1]
            idex1 = idex1+1
    
    return theta        #返回参数

def OLS(xdata,ydata):                          #梯度下降求解
    start = time.clock()
    theta = [0,0]
    iters = 0
    iters = int(iters)
    l = len(ydata)
    l = int(l)
    cost_record = []
    it = []
    sigmal = 0.01
    cost_val = cost(theta,xdata,ydata,l)    #计算代价
    cost_record.append(cost_val)
    it.append(iters)
    while iters <1500:
          theta = gradlient(theta,xdata,ydata,sigmal,l)  #更新参数
          cost_updata = cost(theta,xdata,ydata,l)        #计算代价
          iters = iters + 1
          cost_val = cost_updata         
          cost_record.append(cost_val)                    #记录代价
          it.append(iters)                                #记录迭代次数
    end = time.clock()
    return mat(theta).T,cost_record,it

def show(xArr,yArr):                             #显示回归直线
    plt.xlabel('Population',size=25)             # 横坐标
    plt.ylabel('Profit'    ,size=25)             # 纵坐标
    plt.title('Linear Regression',size=30)       # 标题
    xCopy =xArr.copy()  
    xCopy.sort(0)  
    yHat = xCopy * ws  
    plt.plot(xArr[:,1],yArr,'go',label='y1')   
    plt.plot(xCopy[:,1],yHat,label='y2')  
    plt.show()  

def show1(xArr,yArr):                             #显示代价
    plt.xlabel('iters',size=25)                   # 横坐标
    plt.ylabel('cost' ,size=25)                   # 纵坐标
    plt.title('Linear Regression',size=30)        # 标题
    plt.plot(xArr[0:,],yArr[0:,],'go',label='y1')
    plt.show()

xArr,yArr= loadData()
ws,cost_rec,iters= OLS(xArr,yArr)
test = [1,3.5]
print "人口为35000时,利润为:"
print ws[0][0]*test[0]+ws[1][0]*test[1]
test1 = [1,7]
print "人口为70000时，利润为:"
print ws[0][0]*test1[0]+ws[1][0]*test1[1]
show(xArr,yArr)
show1(mat(np.array(iters)),mat(np.array(cost_rec)))
