import numpy as np
import  matplotlib.pyplot  as  plt
import matplotlib 
plt.rcParams['font.sans-serif'] = 'SimHei'  
labels = np.array(['推进','KDA','生存','输出','综合',"发育"])
data=np.array([7,6,9,7,8,4])
angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
fig=plt.figure(facecolor="white")
plt.subplot(111,polar=True)
plt.plot(angles, data,'o-',linewidth=1, alpha=0.2)
plt.fill(angles, data, alpha=0.25)
plt.thetagrids(angles*180/np.pi,labels)
plt.figtext(0.52, 0.95, 'dota能力分析', ha='center', size=20)
