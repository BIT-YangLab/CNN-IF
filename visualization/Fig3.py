cc_v1_1 = [ 0.372287   ,-0.06701921]
cc_v2_1 = [ 0.3058672 , -0.01781311]
cc_v3_1 = [0.28463867, 0.00688538]
cc_v4_1 = [0.22231029 ,0.00356497]
cc_ffa_1 = [0.17996192 ,0.11115783]
cc_eba_1 = [0.24529971 ,0.19232568]
cc_rsc_1 = [0.19493699 ,0.12288911]
cc_vwfa_1 = [0.14958741 ,0.06681745]

#S2  session=8
cc_v1_2 = [ 0.38177854 ,-0.03781864]
cc_v2_2 = [ 0.26527026 ,-0.00783814]
cc_v3_2 = [0.27372718, 0.00512651]
cc_v4_2 = [0.29753757 ,0.02352532]
cc_ffa_2 = [0.17487279 ,0.0791016 ]
cc_eba_2 = [0.19471303 ,0.14192271]
cc_rsc_2 = [0.24977171 ,0.16070919]
cc_vwfa_2 = [0.14867204 ,0.05960059]

#S3  session=8
cc_v1_3 = [ 0.39203784 ,-0.06597491]
cc_v2_3 = [ 0.32870746 ,-0.05033405]
cc_v3_3 = [ 0.26377004 ,-0.00346276]
cc_v4_3 = [ 0.22688164 ,-0.00124681]
cc_ffa_3 = [0.18743518 ,0.10267865]
cc_eba_3 = [0.19028986 ,0.13705298]
cc_rsc_3 = [0.19497752 ,0.10960349]
cc_vwfa_3 = [0.15942043 ,0.03141425]

#S5  session=8
cc_v1_5 = [0.32709283 ,0.00553336]
cc_v2_5 = [0.28632575, 0.00117348]
cc_v3_5 = [0.2285561 , 0.07446695]
cc_v4_5 = [0.2097014 , 0.10840227]
cc_ffa_5 = [0.19848292 ,0.16174263]
cc_eba_5 = [0.21016163 ,0.15361643]
cc_rsc_5 = [0.24592084 ,0.17729802]
cc_vwfa_5 = [0.17015526 ,0.11451731]

cc_v1_1 = np.expand_dims(cc_v1_1,axis=0)
cc_v1_2 = np.expand_dims(cc_v1_2,axis=0)
cc_v1_3 = np.expand_dims(cc_v1_3,axis=0)
cc_v1_5 = np.expand_dims(cc_v1_5,axis=0)
cc_v1 = np.concatenate([cc_v1_1,cc_v1_2,cc_v1_3,cc_v1_5],axis=0)
cc_v1 = np.mean(cc_v1,axis=0)

cc_v2_1 = np.expand_dims(cc_v2_1,axis=0)
cc_v2_2 = np.expand_dims(cc_v2_2,axis=0)
cc_v2_3 = np.expand_dims(cc_v2_3,axis=0)
cc_v2_5 = np.expand_dims(cc_v2_5,axis=0)
cc_v2 = np.concatenate([cc_v2_1,cc_v2_2,cc_v2_3,cc_v2_5],axis=0)
cc_v2 = np.mean(cc_v2,axis=0)

cc_v3_1 = np.expand_dims(cc_v3_1,axis=0)
cc_v3_2 = np.expand_dims(cc_v3_2,axis=0)
cc_v3_3 = np.expand_dims(cc_v3_3,axis=0)
cc_v3_5 = np.expand_dims(cc_v3_5,axis=0)
cc_v3 = np.concatenate([cc_v3_1,cc_v3_2,cc_v3_3,cc_v3_5],axis=0)
cc_v3 = np.mean(cc_v3,axis=0)

cc_v4_1 = np.expand_dims(cc_v4_1,axis=0)
cc_v4_2 = np.expand_dims(cc_v4_2,axis=0)
cc_v4_3 = np.expand_dims(cc_v4_3,axis=0)
cc_v4_5 = np.expand_dims(cc_v4_5,axis=0)
cc_v4 = np.concatenate([cc_v4_1,cc_v4_2,cc_v4_3,cc_v4_5],axis=0)
cc_v4 = np.mean(cc_v4,axis=0)

cc_ffa_1 = np.expand_dims(cc_ffa_1,axis=0)
cc_ffa_2 = np.expand_dims(cc_ffa_2,axis=0)
cc_ffa_3 = np.expand_dims(cc_ffa_3,axis=0)
cc_ffa_5 = np.expand_dims(cc_ffa_5,axis=0)
cc_ffa = np.concatenate([cc_ffa_1,cc_ffa_2,cc_ffa_3,cc_ffa_5],axis=0)
cc_ffa = np.mean(cc_ffa,axis=0)

cc_eba_1 = np.expand_dims(cc_eba_1,axis=0)
cc_eba_2 = np.expand_dims(cc_eba_2,axis=0)
cc_eba_3 = np.expand_dims(cc_eba_3,axis=0)
cc_eba_5 = np.expand_dims(cc_eba_5,axis=0)
cc_eba = np.concatenate([cc_eba_1,cc_eba_2,cc_eba_3,cc_eba_5],axis=0)
cc_eba = np.mean(cc_eba,axis=0)

cc_rsc_1 = np.expand_dims(cc_rsc_1,axis=0)
cc_rsc_2 = np.expand_dims(cc_rsc_2,axis=0)
cc_rsc_3 = np.expand_dims(cc_rsc_3,axis=0)
cc_rsc_5 = np.expand_dims(cc_rsc_5,axis=0)
cc_rsc = np.concatenate([cc_rsc_1,cc_rsc_2,cc_rsc_3,cc_rsc_5],axis=0)
cc_rsc = np.mean(cc_rsc,axis=0)

cc_vwfa_1 = np.expand_dims(cc_vwfa_1,axis=0)
cc_vwfa_2 = np.expand_dims(cc_vwfa_2,axis=0)
cc_vwfa_3 = np.expand_dims(cc_vwfa_3,axis=0)
cc_vwfa_5 = np.expand_dims(cc_vwfa_5,axis=0)
cc_vwfa = np.concatenate([cc_vwfa_1,cc_vwfa_2,cc_vwfa_3,cc_vwfa_5],axis=0)
cc_vwfa = np.mean(cc_vwfa,axis=0)

plt.figure(figsize=(8,8))
#绘制折线图
plt.plot(x,cc_v1,linewidth=4,label='v1',color='deepskyblue',marker='D',markersize=12)
plt.plot(x,cc_v2,linewidth=4,label='v2',color='black',marker='D',linestyle='-',markersize=12)
plt.plot(x,cc_v3,linewidth=4,label='v3',color='sienna',marker='D',linestyle='-',markersize=12)
plt.plot(x,cc_v4,linewidth=4,label='v4',color='purple',marker='D',linestyle='-',markersize=12)
#
# plt.plot(x,cc_ffa,linewidth=4,label='ffa',color='tomato',marker='D',markersize=12)
# plt.plot(x,cc_eba,linewidth=4,label='eba',color='green',marker='D',linestyle='-',markersize=12)
# plt.plot(x,cc_rsc,linewidth=4,label='rsc',color='gold',marker='D',linestyle='-',markersize=12)
# plt.plot(x,cc_vwfa,linewidth=4,label='vwfa',color='blue',marker='D',linestyle='-',markersize=12)


# plt.hlines(a, 0, 6000, color="k",linestyles='dashed',linewidth=2.5)

plt.xticks(x,x_label,size=32,fontname='Arial',weight='bold') # 设置横坐标的标签
plt.yticks(y,y_label,size=32,fontname='Arial',weight='bold')
plt.grid(axis='x',color='black')#plt.grid(axis='y' 关闭y轴网格线)
ax = plt.gca()
# plt.tick_params(axis='y',width=4,length=4)
#设置坐标轴的标题
# plt.ylabel('Median validation accuracy(R)',size=20)
# plt.xlabel('Training samples',size=30)
# plt.ylim((0,0.45))
#设置图例
font = {'family': 'Arial','weight':'bold','size':30}
# plt.legend(['V1','V2','V3','hV4'],loc='best',facecolor='white',edgecolor='black',fontsize='large',prop=font)

# plt.legend(['FFA','EBA','RSC','VWFA'],loc='best',facecolor='white',edgecolor='black',fontsize='large',prop=font)
#设置坐标轴的刻度
#显示图表
plt.savefig(r'C:\Users\user\Desktop\gnet-data-unpre1.jpg', dpi=2000)
plt.show()