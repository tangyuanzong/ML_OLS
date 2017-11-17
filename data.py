#!/usr/bin/python
#-*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import time

def loadData():
    f=open('ex1data1.txt')                      
    data = f.readlines()                        
    l=len(data)                                
    mat=zeros((l,2))                             
    index=0 
    xdata = ones((l,2))
    ydata = []                       
    for line in data:
        line = line.strip()                     
        linedata = line.split(',')               
        mat[index, :] = linedata[0:2]          
        index +=1
    xdata[:,1] = mat[:,0]
    ydata = mat[:,1]
    return xdata,ydata


def standRegress(xArr,yArr):  
    xMat = mat(xArr); yMat = mat(yArr).T  #.T代表转置矩阵  
    xTx = xMat.T * xMat  
    if linalg.det(xTx) ==0.0: #linalg.det(xTx) 计算行列式的值  
        print "This matrix is singular , cannot do inverse"  
        return  
    ws = xTx.I * (xMat.T * yMat)  
    return ws  

def show(xArr,yArr):
    plt.xlabel('Population',size=25)             # 横坐标
    plt.ylabel('Profit'    ,size=25)             # 纵坐标
    plt.title('Linear Regression',size=30)       # 标题
    yHat = xArr*ws
    xCopy =xArr.copy()  
    xCopy.sort(0)  
    yHat = xCopy * ws  
    plt.plot(xArr[:,1],yArr,'go',label='y1')
    plt.plot(xCopy[:,1],yHat,label='y2')  
    plt.savefig('./plot1.png',format='png')
    #plt.show()  


xArr,yArr= loadData()
ws = standRegress(xArr,yArr)
show(xArr,yArr)
