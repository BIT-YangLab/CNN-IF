import pandas as pd
import csv
import numpy as np
import torch as t
import matplotlib.pyplot as plt
from scipy import stats

from scipy.stats import norm
import pandas
import matplotlib.mlab as mlab

# x = [-0.3,-0.2,-0.1,0.0,0.1,0.2]
# x_label = ['-0.3','-0.2','-0.1','0.0','0.1','0.2']
x = [-0.2,-0.1,0.0,0.1,0.2]
x_label = ['-0.2','-0.1','0.0','0.1','0.2']
alexnet_goal_val_cc_01 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\GNet_goal_subj01_val.txt",dtype=np.float32, delimiter=",")
alexnet_goal_val_cc_02 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\GNet_goal_subj02_val.txt",dtype=np.float32, delimiter=",")
alexnet_goal_val_cc_03 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\GNet_goal_subj03_val.txt",dtype=np.float32, delimiter=",")
alexnet_goal_val_cc_05 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\GNet_goal_subj05_val.txt",dtype=np.float32, delimiter=",")
alexnet_goal = np.concatenate([alexnet_goal_val_cc_01,alexnet_goal_val_cc_02,alexnet_goal_val_cc_03,alexnet_goal_val_cc_05],axis=0)
alexnet_data_val_cc_01 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\GNet_data_subj01_val.txt",dtype=np.float32, delimiter=",")
alexnet_data_val_cc_02 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\GNet_data_subj02_val.txt",dtype=np.float32, delimiter=",")
alexnet_data_val_cc_03 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\GNet_data_subj03_val.txt",dtype=np.float32, delimiter=",")
alexnet_data_val_cc_05 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\GNet_data_subj05_val.txt",dtype=np.float32, delimiter=",")
alexnet_data = np.concatenate([alexnet_data_val_cc_01,alexnet_data_val_cc_02,alexnet_data_val_cc_03,alexnet_data_val_cc_05],axis=0)

gnet_goal_val_cc_01 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\AlexNet_goal_subj01_val.txt",dtype=np.float32, delimiter=",")
gnet_goal_val_cc_02 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\AlexNet_goal_subj02_val.txt",dtype=np.float32, delimiter=",")
gnet_goal_val_cc_03 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\AlexNet_goal_subj03_val.txt",dtype=np.float32, delimiter=",")
gnet_goal_val_cc_05 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\AlexNet_goal_subj05_val.txt",dtype=np.float32, delimiter=",")
gnet_goal = np.concatenate([gnet_goal_val_cc_01,gnet_goal_val_cc_02,gnet_goal_val_cc_03,gnet_goal_val_cc_05],axis=0)
gnet_data_val_cc_01 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\AlexNet_data_subj01_val.txt",dtype=np.float32, delimiter=",")
gnet_data_val_cc_02 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\AlexNet_data_subj02_val.txt",dtype=np.float32, delimiter=",")
gnet_data_val_cc_03 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\AlexNet_data_subj03_val.txt",dtype=np.float32, delimiter=",")
gnet_data_val_cc_05 = np.loadtxt(r"C:\Users\user\Desktop\Fig\Fig2\E\AlexNet_data_subj05_val.txt",dtype=np.float32, delimiter=",")
gnet_data = np.concatenate([gnet_data_val_cc_01,gnet_data_val_cc_02,gnet_data_val_cc_03,gnet_data_val_cc_05],axis=0)

plt.figure(figsize=(7,7))
plt.xticks(x,x_label,size=25,fontname='Arial',weight='bold')#weight='bold'加粗字体
y_label = []
alexnet_compare = alexnet_data-alexnet_goal
gnet_compare = gnet_data-gnet_goal
# plt.xlim(-0.1,0.1)
print(len(alexnet_compare))
print(len(gnet_compare))
mena = [-0.007178729]
alexnet_n,alexnet_bins,alexnet_patches = plt.hist(alexnet_compare,bins=50,zorder=1,density=True,color='dimgrey',edgecolor='white')
gnet_n,gnet_bins,gnet_patches = plt.hist(gnet_compare,bins=50,density=True,color='dimgrey',edgecolor='white')
alexnet_mu = np.mean(alexnet_compare)
alexnet_sigma = np.std(alexnet_compare)
print(alexnet_mu)
print(alexnet_sigma)
gnet_mu = np.mean(gnet_compare)
gnet_sigma = np.std(gnet_compare)
print(gnet_mu)
print(gnet_sigma)

plt.yticks(y_label,size=25)
plt.tick_params(axis='y',width=0,length=0)
alexnet_y=norm.pdf(alexnet_bins,alexnet_mu,alexnet_sigma)#拟合一条最佳正态分布曲线y
plt.plot(alexnet_bins, alexnet_y,color='salmon',linewidth=2.5) #绘制y的曲线
# plt.axvline(-0.039811466,linewidth=2,color='r',label='Noise ceiling',linestyle='--')
gnet_y=norm.pdf(gnet_bins,gnet_mu,gnet_sigma)#拟合一条最佳正态分布曲线y
plt.plot(gnet_bins, gnet_y,color='dodgerblue',linewidth=2.5) #绘制y的曲线
font = {'family': 'Arial','weight':'bold','size':20}
plt.legend(['AlexNet','GNet'],loc='upper right',facecolor='gainsboro',edgecolor='black',fontsize='large',prop=font)
plt.savefig(r'C:\Users\user\Desktop\Fig2d_GNet.jpg', dpi=2000)
plt.show()