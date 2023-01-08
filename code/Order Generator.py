#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as  pd
from datetime import datetime;
import csv
import random as rd


# In[31]:


order_id = 100
stock_symbol_list = ["FB","AAPL","WMT"]
security_type_list = ["EQUITY"]
action_list = ["BUY","SELL"]
base_price_list = {"FB" : [270, 278], "AAPL" : [113, 116], "WMT" : [137, 142]}


# In[32]:



"""
input : customer file path (str) & name (str)
function : extract customer IDs
output : return a list of customer IDs (list)
"""
def readCustomerFile():
    try:
        cust_df = pd.read_csv("C:/Users/hp/Desktop/Untitled Folder/customer.csv")

    except:
        print("Error in opening : " + customer_file_name)
        exit(1)


    list_of_cust_id = cust_df["customerId"].tolist()
    return list_of_cust_id


# In[33]:



"""
input : dictionary with ticker:[min,max] (dict), stock_name(str), quantiy of stock(int), buy/sell(str)
function : alters the dictionary inplace according to change parameter
output : None
"""
def alterPrice(base_price_list, stock_name, quantity, action):

    change_parameter = 0.001

    stock_price_list = base_price_list[stock_name]

    change = change_parameter * quantity
    if(action == "SELL"):
    
        change*=-1
        
    stock_price_list[0] += change
    stock_price_list[1] += change


# In[35]:


"""
input : start of order id (int), customer id list (list), ... (list) , size of cust order table (int)
function : generate random orders and alter price accordingly 
output : list of orders (list)
"""
def generateOrders(customerOrders, order_id, customerID_list, stock_symbol_list, security_type_list, action_list, base_price_list, size_to_generate):
     
    list_of_orders = []
    for i in range(size_to_generate):
        
        stock_name = rd.choice(stock_symbol_list)
        action = rd.choice(action_list)
        quantity = rd.choice(range(50,5000,50))
        new_order = pd.DataFrame(
           {'order_id':order_id, 
            'dateTime':datetime.now(), 
            'custID': rd.choice(customerID_list),         
            'stockSymbol':stock_name,
            'securityType':rd.choice(security_type_list), 
            'action':action, 
            'quantity':quantity,
            'price': rd.uniform(base_price_list[stock_name][0],base_price_list[stock_name][1]),
            'status':'Yes'}, index =[0])
        
        alterPrice(base_price_list, stock_name, quantity, action)
        order_id += 1
        
        customerOrders = pd.concat([new_order, customerOrders]).reset_index(drop = True) 
        
    return customerOrders



# In[38]:


#MAIN

customerID_list = readCustomerFile()

size_to_generate = 10
customerOrders= pd.DataFrame()


# In[40]:


customerOrders = generateOrders(customerOrders,order_id, customerID_list, stock_symbol_list, security_type_list, action_list, base_price_list, size_to_generate)

#TODO post list_of_orders in a csv file

print(customerOrders)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




