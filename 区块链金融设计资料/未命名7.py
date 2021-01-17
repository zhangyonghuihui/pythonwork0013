import  matplotlib.pyplot  as  plt
import pandas as pd
plt.rcParams['font.sans-serif'] = 'SimHei'  
plt.rcParams['axes.unicode_minus'] = False 
df = pd.read_excel('studentscore.xlsx', dtype={'code': 'str'}) 
del df["学号"]
df.boxplot()
plt.figtext(0.52, 0.95, '课程能力分析', ha='center', size=20)
plt.xlabel("科目")
plt.ylabel("分数范围")


