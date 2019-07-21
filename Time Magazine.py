import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

sns.set(color_codes=True)


time_data = pd.read_csv('Magazine.csv',sep=',')
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 202)

# print(time_data.head(5))
# print(time_data.info())
# print(time_data.columns)

time_data['Year_Award'] = time_data['Year'] - time_data['Birth Year']
# print(time_data.head())


#Category counts

category_counts = time_data['Category'].value_counts()
# print(category_counts)
category = category_counts.index
c_counts = category_counts.get_values()
# plt.xticks(rotation=70)
# plt.xlabel('Category Of The Winners')
# plt.ylabel('Number Of Winners')
# plt.title('Number Of Winners Per Category',fontsize=20)
# sns.barplot(x=category,y=c_counts)
# plt.show()


#Category Winner by Country
country_category_group = time_data.groupby(['Country','Category'])
# add_counts = country_category_group.size().unstack()
# normed_subset = add_counts.div(add_counts.sum(1))
# add_counts.plot(kind='barh',figsize=(11,7),stacked=True,colormap='cubehelix')
# plt.show()


#Category Winner by Country Without USA

country_less_usa = time_data[time_data['Country']!='United States']
country_less_usa_category_group = country_less_usa.groupby(['Country','Category'])
# add_counts = country_less_usa_category_group.size().unstack().fillna(0)
# normed_subset = add_counts.div(add_counts.sum(1),axis=0)
# add_counts.plot(kind='barh',legend=True,figsize=(11,7),stacked=True,colormap='cubehelix')
# plt.show()


#Age Of The Winners  By Category

x_val=time_data['Year_Award']
y_val=time_data['Category']
# sns.stripplot(x=x_val,y=y_val,data=time_data,size=10)
# plt.show()

#Age Of Winners Average
year_award_average = time_data['Year_Award'].mean()
# print('The Average is:'+ str(year_award_average)+' Year')


time_data['Year_Lived'] = time_data['Death Year'] - time_data['Birth Year']
# print(time_data[:5])


#Age Ranges Of Winners 4 Age-Categories 1-Youth,2-YoungAdult,3-MiddleAged,4-Senior

max = time_data['Year_Award'].max()
bins = [18,25,35,60,max+1]
age_range = ['Youth','YoungAdult','MiddleAged','Senior']
time_data['Range'] = pd.cut(time_data['Year_Award'],bins)
time_data['Age_Category'] = pd.cut(time_data['Year_Award'],bins,labels=age_range)
# print(time_data.head())

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val=((pct*total/100.0)+0.5)
        return '{p:.2f}% ({v:.2f})'.format(p=pct,v=val)
    return my_autopct



age_category_counts = time_data['Age_Category'].value_counts()
# age_category_counts.plot(kind='pie',legend=True,figsize=(7,7),autopct=make_autopct(age_category_counts))
# plt.show()



#Winners by Country

country_counts = time_data['Country'].value_counts()
# country_counts[:7].plot(kind='pie',legend=True,figsize=(7,7),autopct=make_autopct(country_counts[:6]))
# plt.show()

# sns.jointplot(x=time_data['Year'],y=time_data['Year_Award'])
# plt.show()

#Age Category of thw winners by honor

honor_age_category_group = time_data.groupby(['Honor','Age_Category'])
add_counts = honor_age_category_group.size().unstack().fillna(0)
normed_subset = add_counts.div(add_counts.sum(1),axis=0)
# normed_subset.plot(kind='barh',legend=True,figsize=(10,7),stacked=True,colormap='copper')
# plt.legend(loc='center right')
# plt.show()

#The President Of Egypt
Sadat = time_data[time_data['Title']=='President of Egypt']
print(Sadat)

#The President Of USA
USA_President=time_data[time_data['Title']=='President of the United States']
USA_name=USA_President.groupby(['Category','Name']).size()
print(USA_name)