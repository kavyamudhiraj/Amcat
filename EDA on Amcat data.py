#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_excel(r'F:\data.xlsx')


# In[3]:


df


# In[4]:


df.describe(include="all")


# In[5]:


x=  df.head()
x


# In[6]:


y=df.tail()
y


# In[7]:


df.Designation.value_counts()


# In[8]:


df.Salary.value_counts()


# In[9]:


df.Degree.value_counts()


# In[10]:


df.Specialization.value_counts()


# In[11]:


df['Gender'].value_counts()


# In[12]:


df.info()


# In[13]:


print('maximum: ',df['Salary'].max())


# In[14]:


print("minimum: ",df['Salary'].min())


# In[15]:


df[df['Salary']==df['Salary'].min()]


# In[16]:


df.loc[df.Salary >1000000, :]


# In[17]:


df.loc[df.Salary>1000000,: 'Gender']


# In[19]:


df.loc[(df.Salary > 1000000) & (df.collegeGPA > 80), ['Specialization']]


# In[20]:


df.loc[df.Salary== 1000000,:'Gender']


# In[21]:


df.loc[df.Salary== 1100000,:'Gender']


# In[22]:


df.loc[df.Salary== 1100000,:'Gender']


# In[23]:


df.loc[df.Salary==1200000,:'Gender']


# In[24]:


df.loc[df.Salary==1800000,:'Gender']


# In[25]:


df.loc[df.Salary==2000000,:'Gender']


# In[26]:


df.loc[df.Salary==3000000,:'Gender']


# In[28]:


df[df['CollegeTier'] == df['CollegeTier'].min()]


# In[29]:


df[df['CollegeTier'] == df['CollegeTier'].max()]


# In[30]:


A = df[['10percentage', '12percentage', 'collegeGPA','Specialization', 'Gender']]
print(type(A))
A


# In[32]:


K = df[['English', 'Logical', 'Quant', 'Specialization', 'Gender']]
print(type(K))
K


# In[34]:


df_new= df.groupby('Specialization')
df_new.first()


# In[37]:


df_new.groups.keys()


# In[39]:


df_new.get_group('computer engineering')


# In[41]:


df_new.get_group('electronics and communication engineering')


# In[42]:


df_new.get_group('electrical engineering')


# In[43]:


df_new.get_group('mechanical engineering')


# In[44]:


df_new.get_group('civil engineering')


# In[45]:


df_new.get_group('information technology')


# In[46]:


df_new.get_group('instrumentation and control engineering')


# In[47]:


new_df = df.groupby('Gender')
new_df.first()


# In[48]:


df_new.groups.keys()


# In[51]:


df_new['collegeGPA'].mean()


# In[52]:


df_new.Salary.describe()


# In[53]:


df.loc[df.Gender == 'm', : ]


# In[54]:


df.loc[df.Gender=='f',:]


# In[55]:


df.set_index('Gender',inplace=True)
df.head()


# In[56]:



df.iloc[2]


# In[58]:


df.iloc[3000]


# In[59]:


df.iloc[1, 2]


# In[60]:


df.iloc[7, 7]


# In[62]:


df.iloc[55, 23]


# In[63]:


df.iloc[390, :]


# In[64]:


df.iloc[3, :]


# In[65]:


df.iloc[[2, 3, 6]]


# In[67]:


df.iloc[[2, 3, 6],[1, 2, 3]]


# In[68]:


df.iloc[[2, 3, 6], :]


# In[69]:


df.iloc[3:5]


# In[70]:


df.iloc[:, 4]


# In[71]:


df.iloc[:, 2:4]


# In[72]:



df.iloc[555]


# In[ ]:




