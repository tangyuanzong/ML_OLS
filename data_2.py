#!/usr/bin/python
#-*- coding: utf-8 -*-
from numpy import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time


def loadData():                                 #文件读取函数
    f=open('ex1data2.txt')                      #打开文件    
    data = f.readlines()                        
    l=len(data)                                 #mat为l*3的矩阵,元素都为0
    mat=zeros((l,3))                             
    index=0 
    xdata = ones((l,3))                         #xdata为l*3的矩阵，元素都为1
    ydata = []                       
    for line in data:
        line = line.strip()                     #去除多余字符
        linedata = line.split(',')              #对数据分割
        mat[index, :] = linedata[0:3]           #得到一行数据
        index +=1
    xdata[:,1] = mat[:,0]                       #得到第一列数据
    xdata[:,2] = mat[:,1]                       #得到第二列数据
    ydata = mat[:,2]                            #得到第三列数据
    return xdata,ydata

def model(theta,x):                             #直线方程
    theta = np.array(theta)
    return x.dot(theta)

def cost(theta,xdata,ydata,l):                  #代价函数
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
    return SUM/2/l

def grad(theta,idex1,xdata,ydata,sigmal,l):     #梯度计算
    idex = 0
    SUM = 0
    for line in ydata:
            yp = model(theta,xdata[idex ,:]) - ydata[idex]
            yp =yp * xdata[idex][idex1]
            idex  =idex +1
            SUM = SUM + yp
    return SUM/l


def gradlient(theta,xdata,ydata,sigmal,l):     #参数更新
    idex1 = 0
    for line1 in theta:
            theta[idex1] = theta[idex1] - sigmal * grad(theta,idex1,xdata,ydata,sigmal,l)
            theta[idex1] = theta[idex1]
            idex1 = idex1+1
    
    return theta

def Min_Max(xdata,ydata):                      #归一化数据
    index = 1
    while index < len(xdata[0,:]):
          item = xdata[:,index].max()
          item1 = xdata[:,index].min()
          xdata[:,index] = (xdata[:,index] - item1)/(item-item1)
          index = index+1
    return xdata,ydata
    
def OLS(xdata,ydata):                           #梯度下降求解函数
    start = time.clock()
    theta = [0,0,0]
    iters = 0
    iters = int(iters)
    l = len(ydata)
    l = int(l)
    cost_record = []
    it = []
    sigmal = 0.1
    cost_val = cost(theta,xdata,ydata,l)
    cost_record.append(cost_val)
    it.append(iters)
    while iters <1500:
          theta = gradlient(theta,xdata,ydata,sigmal,l)
          cost_updata = cost(theta,xdata,ydata,l)
          iters = iters + 1
          cost_val = cost_updata
          cost_record.append(cost_val)
          it.append(iters)
    end = time.clock()
    return mat(theta).T,cost_record,it,theta


def show(xArr,yArr,X,Y,thet):                         #显示数据
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.plot(xArr[:,1],xArr[:,2],yArr[0:,],'go',label='z1')
    ax.set_xlabel('Area')
    ax.set_ylabel('Number')
    ax.set_zlabel('Price')
    plt.title('Linear Regression',size=30) 
    x=np.arange(xArr[:,1].min(),xArr[:,1].max(),53.01)
    x1=x.copy()
    y=np.arange(xArr[:,2].min(),xArr[:,2].max(),0.05)
    y1=y.copy()
    idex = 0
    for line in x1:
        x1[idex] = (line - x1.min())/(x1.max()-x1.min())
        idex = idex +1
    idex = 0
    for line in y1:
        y1[idex] = (line - y1.min())/(y1.max()-y1.min())
        idex = idex +1
   
    x,y=np.meshgrid(x,y)
    x1,y1=np.meshgrid(x1,y1)
   
    z = x1[0,:]*thet[0]+x1[1,:]*thet[1]+x1[2,:]*thet[2]
    z[0]=126188.4094911 
    ax.plot_surface(x[0:,],y[0:,],z,rstride=1,cstride=1,cmap='rainbow') 
    plt.show()

def show1(xArr,yArr):                              # 显示cost
    plt.xlabel('iters',size=25)                    # 横坐标
    plt.ylabel('cost',size=25 )                    # 纵坐标  
    plt.title('Linear Regression',size=30)         # 标题
    plt.plot(xArr[0:,],yArr[0:,],'go',label='y1')
    plt.show()

xArr,yArr= loadData()                              #加载数据
xcopy = xArr.copy()                                
ycopy = yArr.copy()
xArr,yArr= Min_Max(xArr,yArr)                      #归一化数据
ws,cost_rec,iters,thet= OLS(xArr,yArr)
test = [1,1650.0,3.0]
test[1] = (test[1]-xcopy[:,1].min())/(xcopy[:,1].max()-xcopy[:,1].min())
test[2] = (test[2]-xcopy[:,2].min())/(xcopy[:,2].max()-xcopy[:,2].min())
print "当房屋的面积为1650平方英尺，房间数量为3时，测的房价为：" 
print test*ws
show(xcopy,ycopy,xArr,yArr,thet)
show1(mat(np.array(iters)),mat(np.array(cost_rec)))
