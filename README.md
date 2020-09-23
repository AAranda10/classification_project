# Predictor Of Churn For Telco Customers

## About the Project

## Goals

-Create a model that will predict the probability of a Telco customer churning or not by using the Telco data from the CodeUp Sequal Database. 

-Identify the drivers that are causing customers to churn to help better understand the customer's needs and prevent further churn.

-Deliver the following: acquire.py, prepare.py, model.pynb and predictions.csv

## Data Dictionary

-customer_id: Unique ID for each customer to keep their information anonymous   

-senior_citizen: Classifies whether a customer is considered to be a senior citizen or not (boolean)

-tenure: Length of time customer has been with company in months

-multiple_lines: Classifies if a customer has multiple phone lines, just one, or none

-internet_service_type_id: Classifies whether a customer purchased fiber optic, dsl, or no internet

-contract_type_id: Categorizes customer's contract type by numerical value i.e. (1: Momth to Month, 2: Annual, 3: 2 Year Contract)

-monthly_charges: Numeric values of what the customer is currently spending monthly based on their services

-total_charges: Numeric values of amount a customer has spent on services in total since signing up

-contract_type: Classifies what contract type a customer is currently enrolled in i.e. Month to Month, Annual, or 2 Year Contract  

-internet_service_type: Classifies the internet service that the customer is currently enrolled in i.e. (Fiber Optic, DSL, No Internet)

-has_churned: Column with 1's and 0's as values identifying whether a customer has churned(1) or has not(0)

-is_male: Column with 1's and 0's as values identifying whether a customer has churned(1) or has not(0)

-has_dependents: Column with 1's and 0's as values identifying whether a customer has dependents(1) or has none(0)    

-has_partner: Column with 1's and 0's as values identifying whether a customer has a partner(1) or has none(0)

-has_phone: Column with 1's and 0's as values identifying whether a customer has at least 1 phone line(1) or has none(0)

-has_dsl: Column with 1's and 0's as values identifying whether a customer has dsl internet(1) or not(0)

-has_fiber: Column with 1's and 0's as values identifying whether a customer has fiber internet(1) or not(0)   

-no_internet: Column with 1's and 0's as values identifying whether a customer has no internet(1) or not(0) 

-has_monthly: Column with 1's and 0's as values identifying whether a customer has a monthly contract(1) or not(0)

-has_annual: Column with 1's and 0's as values identifying whether a customer has an annual contract(1) or not(0)  

-has_two_year: Column with 1's and 0's as values identifying whether a customer has a 2 year contact(1) or not(0)

-only_phone: Column with 1's and 0's as values identifying whether a customer has only phone services(1) or not(0) 

-only_internet: Column with 1's and 0's as values identifying whether a customer has only internet services(1) or not(0) 

-has_multiple: Column with 1's and 0's as values identifying whether a customer has multiple services(1) or not(0) 

-prediction: Column with 1's and 0's as values predicting whether a customer will churn(1) or not(0)

-probability: Returns the probability in percentage of the likelihood that a customer will churn

## Initial Hypotheses & Thoughts

### Thoughts

-My initial thoughts were that there would be a relationship between customers churning and average charges

-Then I wanted to decide whether I would convert the boolean values to 1's and 0's

-Lastly I wanted to figure out what graphs would tell the best story related to the data


### Hypotheses

#### My first hypothesis was that there is a difference between fiber customers monthly charges compared monthly charges for all customers

H0: There is no difference in monthly charges between fiber customers compared to all customers

Ha: There is a difference in monthly charges between fiber customers and customers in general

#### My second hypothesis was that fiber internet customers were not independent of customers who churn

H0: Churn customers are independent of fiber customers

Ha: Churn customers are not independent of fiber customers


#### Project Plan: Breaking it Down

acquire.py

acquire data from csv gathered from github.com/AAranda10/classification_project/

prepare.py from csv gathered from github.com/AAranda10/classification_project/

address missing data
split into train, validate, test

explore

plot correlation matrix of all variables
test each hypothesis

model

try different algorithms: decision tree, logistic regression, random forest, and knn

which features have the most impact?

evaluate on train

select top 4 +/- models to evaluate on validate

select top model

run model on test to verify

conclusion

summarize findings

make recommendations
