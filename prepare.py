#!/usr/bin/env python
# coding: utf-8

# In[38]:


#Were first going to import pandas and 
import pandas as pd
from sklearn.model_selection import train_test_split
from acquire import get_telco_churn_data


# In[39]:


def prep_telco_data(telco):
    telco['has_churned'] = telco.churn.map({'No': 0, 'Yes': 1})
    telco['is_male'] = telco.gender.map({'Male' : 1, 'Female': 0})
    telco['has_dependents'] = telco.dependents.map({'Yes' : 1, 'No': 0})
    telco['has_partner'] = telco.partner.map({'Yes' : 1, 'No': 0})
    telco['has_phone'] = telco.phone_service.map({'Yes' : 1, 'No': 0})
    telco = telco.drop(columns = ['online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'payment_type_id', 'gender', 'dependents', 'phone_service', 'churn', 'partner'])
    telco = telco.loc[:,~telco.columns.duplicated()]
    telco.total_charges = telco.total_charges.str.replace(' ', '0').astype(float)
    telco_dummies1 = pd.get_dummies(telco.internet_service_type)
    telco_dummies2 = pd.get_dummies(telco.contract_type)
    telco_dummies3 = pd.get_dummies(telco.multiple_lines)
    telco = pd.concat([telco, telco_dummies1, telco_dummies2, telco_dummies3], axis = 1)
    train_validate, test = train_test_split(telco, test_size = .2, random_state = 123, stratify = telco.has_churned)
    train, validate = train_test_split(train_validate, test_size = .3, random_state = 123, stratify = train_validate.has_churned)
    return train, validate, test


# In[40]:


train, validate, test = prep_telco_data(get_telco_churn_data())


# In[41]:


train


# In[24]:





# In[ ]:




