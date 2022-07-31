# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 23:58:28 2022

Cyclic Voltammetry
"""

# 铁氰化钾循环伏安法有关性质的测定
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd





plt.style.use("seaborn")
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
fig=plt.figure(figsize=(10,8),dpi=1000)#创建全局绘图区


plt.subplot(2, 2, 1)



df=pd.read_excel(r"D:\学习\barca\仪器分析实验\数据\循环伏安法\text.xlsx")
v=df['x']
biao=['a','b','c','d','e','f']
biaoo=['V=10mV/s','V=20mV/s','V=40mV/s','V=80mV/s','V=100mV/s','V=120mV/s']

for i in range(0,6):
    I=df[str(biao[i])]
    plt.plot(v,I,color=(0.001*i,0.09*i,0.04*i),label=(biaoo[i]))
    


plt.legend()


plt.title("Figure1-不同扫速下电位-电流图 ")
plt.xlabel("电位Potential/V")
plt.ylabel("电流Current/A")


plt.subplot(2, 2, 2)
df=pd.read_excel(r"D:\学习\barca\仪器分析实验\数据\循环伏安法\text2.xlsx")
v=df['x']
biao=['a','b','c','e']
biaoo=['C=1mmol/L','C=2mmol/L','C=5mmol/L','C=10mmol/L']

for i in range(0,4):
    I=df[str(biao[i])]
    plt.plot(v,I,color=(0.12*i,0.004*i,0.09*i),label=(biaoo[i]))
    



plt.title("Figure2-不同浓度下电位-电流图")
plt.xlabel("电位Potential/V")
plt.ylabel("电流Current/A")
plt.legend()

plt.subplot(2, 2, 3)
V=[3.16,	4.47,	6.32	,8.94,	10.00,	10.95]   #扫速
y1=[-481.7,	-643.6,	-842.7	,-1060,	-1141,	-1168]   #还原峰电流ipc(μA)
plt.plot(V,y1,'ro',label="还原峰电流ipc(μA)") 

z= np.polyfit(V,y1,1)
xn = np.linspace( 2 , 12 , 50 )
yn = np.poly1d(z)
plt.plot( xn,yn(xn),V,y1,'ro')

  
y2=[535.2,	638.5,	853.6	,1087	,1168	,1209]  #氧化峰电流ipa(μA)
plt.plot(V,y2,'go',label="氧化峰电流ipa(μA)")
z= np.polyfit(V,y2,1)
xn = np.linspace( 2 , 12 , 50 )
yn = np.poly1d(z)
plt.plot( xn,yn(xn),V,y2,'go')

plt.title("Figure3-峰电流-扫速$\sqrt{V} $图")
plt.xlabel("扫速$\sqrt{V} $/(mV/s)")   #r"$x_0 + v_0t$" \sqrt[n]{3}
plt.ylabel("峰电流/μA")
plt.xlim(2,12)
plt.text(4,1000,"y = 90.123x + 256.45,${R^2}$ = 0.9923")
plt.text(4,-1000,"y = -89.15x - 237.85, ${R^2}$= 0.9917")



plt.subplot(2, 2, 4)

C=[1	,2	,5	,10]   
y1=[-10.40	,-17.00	,-62.40	,-148.00]   #还原峰电流ipc(μA)
plt.plot(C,y1,'ro',label="还原峰电流ipc(μA)") 

z= np.polyfit(C,y1,1)
xn = np.linspace( 0 , 12 , 50 )
yn = np.poly1d(z)
plt.plot( xn,yn(xn),C,y1,'ro')

  
y2=[23.1	,34.3,	91.1	,184.0]  #氧化峰电流ipa(μA)
plt.plot(C,y2,'go',label="氧化峰电流ipa(μA)")
z= np.polyfit(C,y2,1)
xn = np.linspace( 0 , 12 , 50 )
yn = np.poly1d(z)
plt.plot( xn,yn(xn),C,y2,'go')


plt.text(4,150,"y = 18.183x + 1.3031,${R^2}$= 0.9984")
plt.text(4,-150,"y = -15.639x + 10.924,${R^2}$ = 0.9949")

plt.xlabel("铁氰化钾浓度(mmol/L)")
plt.ylabel("峰电流/μA")
plt.title("Figure4-峰电流-浓度工作曲线")
plt.tight_layout()     # 调整子图间距


plt.savefig(r'D:\学习\barca\仪器分析实验\数据\动力学\20211122-F\Y11的图.png')
plt.show()


