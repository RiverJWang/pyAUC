import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1 导入相关库

# 测试样本的数量 ，
parameter = 30
# 2 随机生成结果集
data=pd.DataFrame(index=range(0,parameter),columns=('probability','The true label')) #建立一个表格
data['The true label']=np.random.randint(0,2,size=len(data))   # size是生成data对应的n-by-m矩阵；0,2是生成[0,2)区间
data['probability']=np.random.choice(np.arange(0.1,1,0.1),len(data['probability']))  #np.arange(start 0, stop, step 1) choice


#3 计算混淆矩阵

cm = np.arange(4).reshape(2,2) #生成一组0-3，再放入2by2的矩阵中,定义一个矩阵！或者，初始化np.zeros(2,2)等等

cm[0,0]=len(data[data['The true label']==0][data['probability']<0.5]) #TN  满足data里面==0和<0.5的行，并且用len计数。背住
cm[0,1]=len(data[data['The ture label']==0][data['probability']>=0.5])#FP false positive
cm[1,0]=len(data[data['The ture label']==1][data['probability']<0.5]) #FN false
cm[1,1]=len(data[data['The ture label']==1][data['probability']>=0.5])#TP

# 4 计算假正率和真正率
import itertools #创建高效迭代器的Python模块。
classes = [0,1] #创建一个数组，元组tuple不能修改
plt.figure() #创建图1
plt.imshow(cm,interpolation='nearest',cmap=plt.cm.Blues)  #interpolation 是选取可了nearest插值，cmap是选取了blues图像风格


