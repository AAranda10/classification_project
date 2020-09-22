#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Were first going to import pandas, sklearn and the acquire.py we just created
import pandas as pd
from sklearn.model_selection import train_test_split
from acquire import get_telco_churn_data


# In[13]:


#Were going to create a function that will clean up the telco data to return the format to best work with the models
def prep_telco_data(telco):
    #I first wanted to create columns that would replace the strings with numeric values of 1's and 0's
    telco['has_churned'] = telco.churn.map({'No': 0, 'Yes': 1})
    telco['is_male'] = telco.gender.map({'Male' : 1, 'Female': 0})
    telco['has_dependents'] = telco.dependents.map({'Yes' : 1, 'No': 0})
    telco['has_partner'] = telco.partner.map({'Yes' : 1, 'No': 0})
    telco['has_phone'] = telco.phone_service.map({'Yes' : 1, 'No': 0})
    #Then I wanted to drop all the columns I don't feel were relevant to discovery of customer churn
    #Based on prior knowledge, most customers are mainly focused on experience, price, product availability, and performance
    #So I wanted to remove the columns that didn't have much of an impact on price since we didn't have information on the other reasoning
    #I also removed duplicate columns
    telco = telco.drop(columns = ['online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'payment_type_id', 'gender', 'dependents', 'phone_service', 'churn', 'partner'])
    telco = telco.loc[:,~telco.columns.duplicated()]
    #I noticed that there were 11 rows that had a white space rather than a number
    #This represented new customers and because they were under contract, they are valuable customers to predict whether they would churn or not
    #Rather than deleting them, I chose to replace their total charges to zero because they signed a contract and have not been billed
    #Based on experience with providers, typically they do not charge until after use, therefore these customers are unchurned customers that have not been billed yet
    telco.total_charges = telco.total_charges.str.replace(' ', '0').astype(float)
    #Then I created dummies columns for internet type, contract type and multiple lines to make it easier to compare the sub catagories later
    telco_dummies1 = pd.get_dummies(telco.internet_service_type)
    telco_dummies2 = pd.get_dummies(telco.contract_type)
    telco_dummies3 = pd.get_dummies(telco.multiple_lines)
    #Then I concated the dummies to my existing dataframe so I have everything in one place
    telco = pd.concat([telco, telco_dummies1, telco_dummies2, telco_dummies3], axis = 1)
    telco = telco.rename(columns = {'DSL':'has_dsl', 'Fiber optic': 'has_fiber', 'None': 'no_internet', 'Month-to-month': 'has_monthly', 'One year': 'has_annual', 'Two year': 'has_two_year', 'No': 'only_phone', 'No phone service': 'only_internet', 'Yes': 'has_multiple'})
    #Lastly, I split the data into train, validate and test so i could more effectively create my model
    train_validate, test = train_test_split(telco, test_size = .2, random_state = 123, stratify = telco.has_churned)
    train, validate = train_test_split(train_validate, test_size = .3, random_state = 123, stratify = train_validate.has_churned)
    return train, validate, test


# In[14]:


#Here I was just testing to make sure my function worked before I exported it as a csv
train, validate, test = prep_telco_data(get_telco_churn_data())


# In[15]:


train


# In[ ]:





# In[ ]:




