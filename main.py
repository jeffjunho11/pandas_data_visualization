#한국 연도별 GDP 변화
"""
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

#폰트설정
font_path = "./타이포 쌍문동 B.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#엑셀 불러오기
df = pd.read_excel('연도별2011.xlsx')
ndf = df.iloc[0,1:]

ndf.index = ndf.index.map(int)
ndf = ndf[ndf.index >= 2013] #2013년도부터만 사용

#plt.figure(figsize=(14,5))
#plt.xticks(rotation = 'vertical')

plt.plot(ndf.index, ndf.values)

plt.title('한국 연도별 GDP 변화')

plt.xlabel('기간')
plt.ylabel('GDP')

plt.legend(labels=['한국'])

plt.show()

"""
"""
# GDP와 행복지수 산점도

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

plt.style.use('default')

#폰트설정
font_path = "./타이포 쌍문동 B.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#행복지수 엑셀 불러오기
df = pd.read_excel('국가별행복지수.xlsx')
ndf = df.loc[:,['Country', 'happiness2020','pop2021']]

#DP 엑셀 불러오기
df2 = pd.read_excel('GDP_Processing.xlsx')
df2.columns = ['Code','Rank','Country','GDP']
ndf2 = df2.loc[:,['Country','GDP']]

#두 지수 합치기
res = pd.merge(ndf, ndf2)
#print(res)

#행 인데스 -> 열 이름

#res = res.T
#res = res.rename(columns=res.iloc[0])
#res = res.drop(res.index[0])
#print(res)

#미국과 중국 제거
res = res[res['Country'] != 'United States']
res = res[res['Country'] != 'China']
res = res[res['Country'] != 'Japan']
res = res[res['Country'] != 'Germany']


#디자인
cylinders_size = res.pop2021/res.pop2021.max() * 300

#데이터 시각화
res.plot(kind='scatter', x='GDP', y='happiness2020', c = 'b', alpha=0.7)
plt.title('Scatter Plot - happiness vs GDP')
plt.show()


"""
"""
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

#폰트설정
font_path = "./타이포 쌍문동 B.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#엑셀 불러오기
df = pd.read_excel('연도별2011.xlsx')
ndf = df.iloc[0,1:]

ndf.index = ndf.index.map(int)
ndf = ndf[ndf.index >= 2013] #2013년도부터만 사용

#데이터프레임
df2 = pd.Series({'2013':6.27, '2014':5.98, '2015':5.84,'2016':5.83,'2017':5.87,'2018':5.89,'2019':5.87,'2020':5.84})
df2.index = df2.index.map(int)


fig, axe1 = plt.subplots()
axe2 = axe1.twinx()

c1 = axe1.plot(ndf.index, ndf.values, color='b')
c2 = axe2.plot(df2.index, df2.values, color='r')

axe1.set_ylabel('GDP')
axe2.set_ylabel('행복지수')

plt.title('한국 \'행복지수 & GDP\' 변화')

plt.xlabel('기간')
plt.ylabel('행복지수')

c = c1 + c2
plt.legend(c, ['GDP','행복지수'])

plt.show()


"""
"""
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

#폰트설정
font_path = "./타이포 쌍문동 B.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


#지니 엑셀 불러오기
df = pd.read_excel('GINI.xlsx')
ndf = df.loc[:,['Country','giniCoefficient']]

#행복지수 엑셀 불러오기
df2 = pd.read_excel('국가별행복지수.xlsx')
ndf2 = df2.loc[:,['Country', 'happiness2020','pop2021']]

#두 지수 합치기
res = pd.merge(ndf, ndf2)
#print(res)

#행 인데스 -> 열 이름

#res = res.T
#res = res.rename(columns=res.iloc[0])
#res = res.drop(res.index[0])
#print(res)

#미국과 중국 제거
#res = res[res['Country'] != 'United States']
#res = res[res['Country'] != 'China']

#디자인
#cylinders_size = res.pop2021/res.pop2021.max() * 300

#데이터 시각화
res.plot(kind='scatter', x='giniCoefficient', y='happiness2020',c = 'coral')
plt.title('Scatter Plot - happiness vs 빈부격차')
plt.show()

"""

"""
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

#폰트설정
font_path = "./타이포 쌍문동 B.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


#GDP per CAPITA 엑셀 불러오기
df = pd.read_excel('gdp_per_capita.xls')
ndf = df.loc[0:,['Country','2020']]

#ndf = df.loc[:,['Country','giniCoefficient']]

#행복지수 엑셀 불러오기
df2 = pd.read_excel('국가별행복지수.xlsx')
ndf2 = df2.loc[:,['Country', 'happiness2020','pop2021']]


#두 지수 합치기
res = pd.merge(ndf, ndf2)
print(res)

"""
#행 인데스 -> 열 이름

#res = res.T
#res = res.rename(columns=res.iloc[0])
#res = res.drop(res.index[0])
#print(res)

#미국과 중국 제거
#res = res[res['Country'] != 'United States']
#res = res[res['Country'] != 'China']

#디자인
#cylinders_size = res.pop2021/res.pop2021.max() * 300
"""

#데이터 시각화
res.plot(kind='scatter', x='2020', y='happiness2020',c = 'coral')
plt.title('Scatter Plot - happiness vs 1인당GDP')
plt.xlabel('1인당 GDP')
plt.show()
"""

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

#폰트설정
font_path = "./타이포 쌍문동 B.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


#GDP per CAPITA 엑셀 불러오기
df = pd.read_excel('언론자유지수.xlsx')
ndf = df.loc[:,['Country','Score 2020']]

#ndf. = ndf['Score 2020'].map(int)

#ndf = df.loc[:,['Country','giniCoefficient']]

#행복지수 엑셀 불러오기
df2 = pd.read_excel('국가별행복지수.xlsx')
ndf2 = df2.loc[:,['Country', 'happiness2020','pop2021']]


#두 지수 합치기
res = pd.merge(ndf, ndf2)
print(res)


#행 인데스 -> 열 이름

#res = res.T
#res = res.rename(columns=res.iloc[0])
#res = res.drop(res.index[0])
#print(res)

#미국과 중국 제거
#res = res[res['Country'] != 'United States']
#res = res[res['Country'] != 'China']

#디자인
#cylinders_size = res.pop2021/res.pop2021.max() * 300


#데이터 시각화
res.plot(kind='scatter', x='Score 2020', y='happiness2020',c = 'coral')
plt.title('Scatter Plot - happiness vs 언론자유지수')
plt.xlabel('언론자유지수')
plt.show()


