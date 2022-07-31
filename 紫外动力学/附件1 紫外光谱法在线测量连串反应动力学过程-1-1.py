#  紫外光谱法在线测量连串反应动力学过程

import numpy as np
import matplotlib.pyplot as plt
y=np.loadtxt(r"D:\学习\barca\化学信息学\课堂项目CHEMCAM MSL LIBS\data.txt")
time=np.loadtxt(r"D:\学习\barca\仪器分析实验\数据\动力学\X2.txt")
wavelength=np.arange(255,301,1)


#ITTFA类的使用  迭代目标转换因子分析，定性分析
import numpy as np
# 读水解紫外数据
#X=np.loadtxt ("D:\\学习\\barca\\化学信息学\\化学信息学\\仪器联用—高维数据分析\\例子-邻苯二甲酸二甲酯的水解\\shuijie.txt")                  #    "D:\\学习\\barca\\仪器分析实验\\数据\\动力学\\20211122-F\\Y1.txt"
X=np.loadtxt (r"D:\学习\barca\仪器分析实验\数据\动力学\20211122-F\Y11.txt")
X=X.T
#X=X[:,10:50]  #取波长260~300
from ITTFA import ITTFA
#构造ITTFA算法对象
ittfa=ITTFA(X)
#特征值分析，相邻特征值比值，获取组分数k1
lamdaInfo=ittfa.getEigenValueInfo()  #特征值分析
k=int(input('组分数：'))  #k=3
ittfa.PCAdecompose(k)  #获取有效信息，去掉噪声
nsresult,minLocation=ittfa.needleSearch()  # 针式搜索
#  制作搜索，寻找最小点
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm
plt.style.use("seaborn")
#制作针式搜索结果曲线
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体为黑体
fig=plt.figure(figsize=(10,8),dpi=300)#创建全局绘图区


plt.subplot(2, 2, 1)
for i in range(0,43):
    plt.plot(wavelength,X[i,:])
plt.title("Figure1-反应体系的紫外吸收光谱图")
plt.xlabel("Wavelength/nm")
plt.ylabel("Intensity")



plt.subplot(2, 2, 2)
plt.plot(nsresult)
plt.title("Figure2-针式搜索结果曲线")


plt.subplot(2, 2, 3)
C,S=ittfa.getCS(minLocation)  # 获取纯谱CS
plt.plot(time,C)   
plt.title("Figure3-动力学谱图")
plt.xlabel("Time/s")
plt.ylabel("Concentration mol/L")

plt.subplot(2, 2, 4)
plt.plot(wavelength,S)
plt.xlabel("Wavelength/nm")
plt.ylabel("Intensity")
plt.title("Figure4-纯谱图")
plt.tight_layout()     # 调整子图间距


plt.savefig(r'D:\学习\barca\仪器分析实验\数据\动力学\20211122-F\Y11的图.png')
plt.show()





'''
CBBL算法—灰色体系的定量分析  
'''

import numpy as np
import random
# 评估函数
'''
X=X.shape
n=X.size(axis=0)
m=X.size(axis=0)'''
size=X.shape
print(size[0],size[1])  #size[0]行数,size[1]列数
n=size[0]
m=size[1]
#print(m,'\n',n)
def func(X,pcs):  # 矩阵X，提取pcs主成分后残差标准差
    B = np.linalg.svd(X,full_matrices=False)
    err1=B[1][pcs:]
    err=np.sqrt( (err1**2).sum()/(n*m-1)  )
    return err
M=np.loadtxt ("D:\\学习\\barca\\化学信息学\\化学信息学\\仪器联用2\\mix_2混合物.txt")  #混合物矩阵
X=np.loadtxt ("D:\\学习\\barca\\化学信息学\\化学信息学\\仪器联用2\\m1_2组分1.txt")  #组分A谱
B = np.linalg.svd(M,full_matrices=False)
lamda = B[1]
for i in range(len(lamda)-1):
    print(lamda[i]/lamda[i+1])  #确定体系组分数
k=int(input('请确定主成分数='))
x0=1
L=M-X*x0
k=k-1    # 从 L 矩阵求解的特征值数

y0=func(L,k)
count=0
while count<100:
    delta=(random.random()-0.5)/10.0  # 值变化的小一点，避免跳跃
    x1=x0+delta
    L=M-X*x1
    y1=func(L,k)
    if (y1<y0):
        x0=x1;    y0=y1
    print("第",count,"次迭代，","x=",x0,"  y=",y0)
    count +=1