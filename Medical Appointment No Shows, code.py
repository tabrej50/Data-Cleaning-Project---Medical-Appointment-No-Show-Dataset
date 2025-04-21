#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

df = pd.read_csv("C:\\Users\\Parvej\\Downloads\\Medical Appointment No Shows.csv")
df.head()


# In[8]:


df.info()

print(df.isnull().sum())

print("Duplicates:", df.duplicated().sum())

df.describe()


# In[9]:


df = df.drop_duplicates()

df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print(df['gender'].value_counts())

df = df[df['age'] >= 0]

df = df.drop(columns=['patientid', 'appointmentid'])

df.info()


# In[10]:


df.to_csv('cleaned_medical_appointments.csv', index=False)


# In[ ]:




