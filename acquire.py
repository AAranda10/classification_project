#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First you will need an env.py file with your host, password, and username information to access the CodeUp Database
#You will need to ensure this is saved within a .gitignore file so your password information is not made public
from env import host, password, user

#Here we will define a function that will access the database and import your data to your notebook
def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[2]:


#We will need to import pandas as pd in order to convert the Sql data into a Pandas Dataframe
import pandas as pd

#Here we will create the SQL Query to return all of the data we will want to assess, in this case it is the Telco_Churn Dataset
#We are also going to join on the contract types and internet types tables so we can reference what the numeric values mean in the customer table for those columns
sql_query = 'SELECT * FROM customers JOIN contract_types ON customers.contract_type_id = contract_types.contract_type_id JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id'

#Here we will create a function that will access the database, and apply the query so when it is ran, you will get the same formatting
def get_telco_churn_data():
    return pd.read_sql(sql_query, get_connection('telco_churn'))


# In[3]:


#Here we are testing to make sure the functions work and are returning the correct data since we will be using this later
#Save as a CSV and put into your folder for quicker use later
telco = get_telco_churn_data()
telco.head()


# In[ ]:





# In[ ]:




