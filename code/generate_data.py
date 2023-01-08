"""
Author : Shriniwas Nayak, Saloni Agiwal
Date : 9th Sept 2020
"""

import pandas as pd
import csv
import random as rd
from datetime import datetime
import time


customer_file_name = "customer.csv"
customerOrderFileName = "customerOrder.csv"
brokerFileName = "broker.csv"
tradeBookFileName = "tradebook.csv"

#CHANGE PATH AS PER DIRECTORY & OS
customer_file_path = "/home/shriniwas/UBSProj/input/"
customerOrderFilePath = "/home/shriniwas/UBSProj/input/"
brokerFilePath = "/home/shriniwas/UBSProj/input/"
tradeBookFilePath = "/home/shriniwas/UBSProj/input/"

largeOrderThreshold = 3500

order_id = 100

stock_symbol_list = ["FB","AAPL","WMT"]

security_type_list = ["EQUITY"]

action_list = ["BUY","SELL"]

base_price_list = {"FB" : [270, 278], "AAPL" : [113, 116], "WMT" : [137, 142]}

trade_id = 1000

firm_id = 50

l = 0.200

g = 0.600


"""
input : customer file path (str) & name (str)
function : extract customer IDs
output : return a list of customer IDs (list)
"""

def readCustomerFile(customer_file_path, customer_file_name):

	try:

		cust_df = pd.read_csv(customer_file_path + customer_file_name)

	except:
	
		print("Error in opening : " + customer_file_name)
		exit(1)


	list_of_cust_id = cust_df["customerId"].tolist()
	
	return list_of_cust_id


	
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



"""
"""
def thresholdCheck(quantity):

	global largeOrderThreshold

	return quantity > largeOrderThreshold



"""
"""
def generateFirmOrderFR(custOrder, base_price_list):

	listOfFirmOrders = []

	if(custOrder["action"] == "SELL"):
	
		action = "SELL"
	
		new_order = pd.DataFrame(
           {'stockSymbol':custOrder["stockSymbol"],
            'securityType':custOrder["securityType"], 
            'action':action, 
            'quantity':custOrder["quantity"],
            'price': custOrder["price"]}, index =[0])
        
		alterPrice(base_price_list, custOrder["stockSymbol"], custOrder["quantity"], action)
        
		listOfFirmOrders.append(new_order)
		
	else:
	
		action = "BUY"
	
		new_order_b = pd.DataFrame(
           {'stockSymbol':custOrder["stockSymbol"],
            'securityType':custOrder["securityType"], 
            'action':action, 
            'quantity':custOrder["quantity"],
            'price': custOrder["price"]}, index =[0])
        
		alterPrice(base_price_list, custOrder["stockSymbol"], custOrder["quantity"], action)
        
		listOfFirmOrders.append(new_order_b)
		
		action = "SELL"
		
		new_order_s = pd.DataFrame(
           {'stockSymbol':custOrder["stockSymbol"],
            'securityType':custOrder["securityType"], 
            'action':action, 
            'quantity':custOrder["quantity"],
            'price': custOrder["price"] + (0.01*base_price_list[custOrder["stockSymbol"]][1])}, index =[0])
	
	
		alterPrice(base_price_list, custOrder["stockSymbol"], custOrder["quantity"], action)
	
		listOfFirmOrders.append(new_order_s)

	return listOfFirmOrders



"""
"""
def generateFirmOrder(stock_symbol_list, security_type_list, action_list, base_price_list, size_to_generate):

	stock_name = rd.choice(stock_symbol_list)
		
	action = rd.choice(action_list)
		
	quantity = rd.choice(range(50,5000,50))

	price = rd.uniform(base_price_list[stock_name][0],base_price_list[stock_name][1])

	new_order = pd.DataFrame(
           {'stockSymbol':stock_name,
            'securityType':rd.choice(security_type_list), 
            'action':action, 
            'quantity':quantity,
            'price': price}, index =[0])
            
	alterPrice(base_price_list, stock_name, quantity, action)

	return new_order
	

"""
input : empty Data Frame (pandas.DataFrame()) start of order id (int), customer id list (list), ... (list) , size of cust order table (int)
function : generate random orders and alter price accordingly 
output : list of orders (list)
"""
def generateOrders(order_id, customerID_list, stock_symbol_list, security_type_list, action_list, base_price_list, size_to_generate):

	customerOrders = pd.DataFrame()
	
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
	
		
		time.sleep(rd.uniform(l,g))
	
	return customerOrders


"""
"""
def readBrokerFile(brokerFilePath, brokerFileName):

	try:

		broker_df = pd.read_csv(brokerFilePath + brokerFileName)

	except:
	
		print("Error in opening : " + brokerFileName)
		exit(1)


	listOfBrokerID = broker_df["brokerId"].tolist()
	
	return listOfBrokerID

"""
"""
def addOrders(listOfFirmOrders, custOrder, brokerIDList):

	global trade_id

	fraud_df = pd.DataFrame()


	if(len(listOfFirmOrders) > 1):
	
	
		firmOrder = listOfFirmOrders[0]
		new_df = pd.DataFrame({'trade_id':trade_id, 
						'dateTime':datetime.now(), 
						'F/C': "FIRM",
						'ID' : firm_id,       
						'stockSymbol': firmOrder["stockSymbol"],
						'securityType': firmOrder["securityType"], 
						'action': firmOrder["action"], 
						'quantity':firmOrder["quantity"],
						'price': firmOrder["price"],
						'brokerID' : rd.choice(brokerIDList)},index =[0])
	
		print("ID : {0}".format(trade_id) )
			
		trade_id += 1
		
		time.sleep(rd.uniform(l,g))
		
		fraud_df = pd.concat([new_df, fraud_df]).reset_index(drop = True)
		
		new_df = pd.DataFrame(
					   {'trade_id':trade_id, 
						'dateTime':datetime.now(), 
						'F/C': "CUSTOMER",
						'ID' : custOrder["custID"],       
						'stockSymbol': custOrder["stockSymbol"],
						'securityType': custOrder["securityType"], 
						'action':custOrder["action"], 
						'quantity':custOrder["quantity"],
						'price': custOrder["price"],
						'brokerID' : rd.choice(brokerIDList)},index =[0])
						
		trade_id += 1
		
		time.sleep(rd.uniform(l,g))
		
		fraud_df = pd.concat([new_df, fraud_df]).reset_index(drop = True)
		
		firmOrder = listOfFirmOrders[1]
		new_df = pd.DataFrame({'trade_id':trade_id, 
						'dateTime':datetime.now(), 
						'F/C': "FIRM",
						'ID' : firm_id,       
						'stockSymbol': firmOrder["stockSymbol"],
						'securityType': firmOrder["securityType"], 
						'action': firmOrder["action"], 
						'quantity':firmOrder["quantity"],
						'price': firmOrder["price"],
						'brokerID' : rd.choice(brokerIDList)},index =[0])
			
		trade_id += 1
		
		fraud_df = pd.concat([new_df, fraud_df]).reset_index(drop = True)
		
		
	else:
	
		firmOrder = listOfFirmOrders[0]
		new_df = pd.DataFrame({'trade_id':trade_id, 
						'dateTime':datetime.now(), 
						'F/C': "FIRM",
						'ID' : firm_id,       
						'stockSymbol': firmOrder["stockSymbol"],
						'securityType': firmOrder["securityType"], 
						'action': firmOrder["action"], 
						'quantity':firmOrder["quantity"],
						'price': firmOrder["price"],
						'brokerID' : rd.choice(brokerIDList)},index =[0])
		
		print("ID : {0}".format(trade_id) )
			
		trade_id += 1
		
		time.sleep(rd.uniform(l,g))
		
		fraud_df = pd.concat([new_df, fraud_df]).reset_index(drop = True)
		
		new_df = pd.DataFrame(
					   {'trade_id':trade_id, 
						'dateTime':datetime.now(), 
						'F/C': "CUSTOMER",
						'ID' : custOrder["custID"],       
						'stockSymbol': custOrder["stockSymbol"],
						'securityType': custOrder["securityType"], 
						'action':custOrder["action"], 
						'quantity':custOrder["quantity"],
						'price': custOrder["price"],
						'brokerID' : rd.choice(brokerIDList)},index =[0])
				
						
		trade_id += 1
		
		fraud_df = pd.concat([new_df, fraud_df]).reset_index(drop = True)
	
		
	return fraud_df
	
		

"""
"""
def generateTradeBook(customerOrders, brokerIDList):

	global trade_id

	tradeBook = pd.DataFrame()

	for i in range(len(customerOrders)):
		
		custOrder = customerOrders.loc[i]
		
		
		if(thresholdCheck(custOrder["quantity"])):
		
			if( bool( rd.choices([0,1], weights = [0.5, 0.5], k = 1)[0] ) ):
			
				listOfFirmOrders = generateFirmOrderFR(custOrder, base_price_list)
				new_df = addOrders(listOfFirmOrders, custOrder, brokerIDList)
				tradeBook = pd.concat([new_df, tradeBook]).reset_index(drop = True)
				
			else:
			
				firmOrder = generateFirmOrder(stock_symbol_list, security_type_list, action_list, base_price_list, size_to_generate)
				new_df = pd.DataFrame(
					   {'trade_id':trade_id, 
						'dateTime':datetime.now(), 
						'F/C': "FIRM",
						'ID' : firm_id,       
						'stockSymbol': firmOrder["stockSymbol"],
						'securityType': firmOrder["securityType"], 
						'action': firmOrder["action"], 
						'quantity':firmOrder["quantity"],
						'price': firmOrder["price"],
						'brokerID' : rd.choice(brokerIDList)},index =[0])
						
				trade_id += 1	
				
				tradeBook = pd.concat([new_df, tradeBook]).reset_index(drop = True)
				
		else:
		
			new_df = pd.DataFrame(
					   {'trade_id':trade_id, 
						'dateTime':datetime.now(), 
						'F/C': "CUSTOMER",
						'ID' : custOrder["custID"],       
						'stockSymbol': custOrder["stockSymbol"],
						'securityType': custOrder["securityType"], 
						'action':custOrder["action"], 
						'quantity':custOrder["quantity"],
						'price': custOrder["price"],
						'brokerID' : rd.choice(brokerIDList)},index =[0])
						
			trade_id += 1
			
			tradeBook = pd.concat([new_df, tradeBook]).reset_index(drop = True)
			
		time.sleep(rd.uniform(l,g))
							
				
	return tradeBook
				
				


#MAIN

customerID_list = readCustomerFile(customer_file_path, customer_file_name)

brokerIDList = readBrokerFile(brokerFilePath, brokerFileName)

size_to_generate = 100


customerOrders = generateOrders(order_id, customerID_list, stock_symbol_list, security_type_list, action_list, base_price_list, size_to_generate)
customerOrders.to_csv(customerOrderFilePath + customerOrderFileName, index = False)
tradeBook = generateTradeBook(customerOrders, brokerIDList)
tradeBook.to_csv(tradeBookFilePath + tradeBookFileName, index = False)




