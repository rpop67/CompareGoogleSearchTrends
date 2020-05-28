#connect to google
from pytrends.request import TrendReq

list1=['Stranger Things','Friends', 'Riverdale','Game of Thrones', 'The office']
list2=['The office', 'Breaking Bad' ,'Money Heist','Peaky Blinders' ,'Black Mirror']
#connecting list1 and list2 to Google Trends Search resp
pytrends1=TrendReq()
pytrends2=TrendReq()
#build payload;setting location to US and timeframe of 1 year
pytrends1.build_payload(list1,geo='US',timeframe="today 12-m")
pytrends2.build_payload(list2,geo='US',timeframe="today 12-m")
#interest_over_time method returns pandas.DataFrame

df1=pytrends1.interest_over_time()
df2=pytrends2.interest_over_time()

# print("************** DF1************* :\n",df1.head(),"\n************** DF2*************\n",df2.head())
averageList1=[]
averageList2=[]
for item in list1:
    averageList1.append(df1[item].mean().round(0))

for item in list2:
    averageList2.append(df2[item].mean().round(0))
# print("averageList1 : ",averageList1,"\naverageList2 : ",averageList2)

normalizationFactor=averageList1[0]/averageList2[0]

for i in range(len(averageList2)):
    normalisedVal=normalizationFactor*averageList2[i]
    averageList2[i]=normalisedVal.round(0)
# print("averageList1 : ",averageList1,"\naverageList2 : ",averageList2)

averageList2.pop(0)
list2.pop(0)
# Combine list of TVSeries i.e. list 1 and list 2
TVSeriesList=list1+list2
# Combine list of AverageLists i.e. averageList1 and averageList2
finalAverageList=averageList1+averageList2
# print("TVSeriesList : ",TVSeriesList,"\nFinalAverageList : ",finalAverageList)

#plotting barchart
import numpy as np
import matplotlib.pyplot as plt
y_pos=np.arange(len(TVSeriesList))
plt.barh(y_pos,finalAverageList,align='center',alpha=0.5)
plt.yticks(y_pos,TVSeriesList)
plt.xlabel('Average popularity')
plt.show()
