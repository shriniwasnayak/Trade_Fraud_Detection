"""

Date : 10th Sept 2020
Author : Shriniwas Nayak, Akshat Mehta, Shweta Barge

"""

from datetime import datetime


potentialList =[{'trade_id': '1082', 'trade_date': '16-09-2020', 'trade_time': '15:21:21', 'Client_Type': 'CUSTOMER', 'Client_ID': '104', 'stockSymbol': 'FB', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '4500', 'price': '279.78', 'brokerID': '4'}, {'trade_id': '1102', 'trade_date': '16-09-2020', 'trade_time': '15:21:52', 'Client_Type': 'CUSTOMER', 'Client_ID': '103', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4900', 'price': '55.26', 'brokerID': '1'}, {'trade_id': '1127', 'trade_date': '16-09-2020', 'trade_time': '15:22:27', 'Client_Type': 'CUSTOMER', 'Client_ID': '102', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4700', 'price': '74.92', 'brokerID': '3'}, {'trade_id': '1132', 'trade_date': '16-09-2020', 'trade_time': '15:22:34', 'Client_Type': 'CUSTOMER', 'Client_ID': '102', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3650', 'price': '293.26', 'brokerID': '1'}, {'trade_id': '1143', 'trade_date': '16-09-2020', 'trade_time': '15:22:48', 'Client_Type': 'CUSTOMER', 'Client_ID': '105', 'stockSymbol': 'AAPL', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '4150', 'price': '136.61', 'brokerID': '1'}, {'trade_id': '1172', 'trade_date': '16-09-2020', 'trade_time': '15:23:32', 'Client_Type': 'CUSTOMER', 'Client_ID': '101', 'stockSymbol': 'WMT', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '4700', 'price': '171.36', 'brokerID': '4'}, {'trade_id': '1183', 'trade_date': '16-09-2020', 'trade_time': '15:23:49', 'Client_Type': 'CUSTOMER', 'Client_ID': '101', 'stockSymbol': 'AAPL', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '4750', 'price': '177.96', 'brokerID': '3'}]






firmTradeList = [{'trade_id': '1213', 'trade_date': '16-09-2020', 'trade_time': '15:24:34', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2600', 'price': '121.98', 'brokerID': '3'}, {'trade_id': '1211', 'trade_date': '16-09-2020', 'trade_time': '15:24:31', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '4900', 'price': '172.09', 'brokerID': '4'}, {'trade_id': '1209', 'trade_date': '16-09-2020', 'trade_time': '15:24:28', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '4050', 'price': '187.56', 'brokerID': '2'}, {'trade_id': '1191', 'trade_date': '16-09-2020', 'trade_time': '15:24:01', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '500', 'price': '175.41', 'brokerID': '4'}, {'trade_id': '1187', 'trade_date': '16-09-2020', 'trade_time': '15:23:55', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '1950', 'price': '288.01', 'brokerID': '2'}, {'trade_id': '1184', 'trade_date': '16-09-2020', 'trade_time': '15:23:50', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'FUTURES', 'trade_action': 'SELL', 'quantity': '4750', 'price': '183.09', 'brokerID': '1'}, {'trade_id': '1182', 'trade_date': '16-09-2020', 'trade_time': '15:23:47', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '4750', 'price': '154.34', 'brokerID': '3'}, {'trade_id': '1175', 'trade_date': '16-09-2020', 'trade_time': '15:23:36', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3200', 'price': '180.83', 'brokerID': '4'}, {'trade_id': '1174', 'trade_date': '16-09-2020', 'trade_time': '15:23:34', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '650', 'price': '178.65', 'brokerID': '3'}, {'trade_id': '1173', 'trade_date': '16-09-2020', 'trade_time': '15:23:33', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3150', 'price': '178.99', 'brokerID': '5'}, {'trade_id': '1171', 'trade_date': '16-09-2020', 'trade_time': '15:23:30', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3150', 'price': '152.28', 'brokerID': '2'}, {'trade_id': '1166', 'trade_date': '16-09-2020', 'trade_time': '15:23:23', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '350', 'price': '306.19', 'brokerID': '2'}, {'trade_id': '1162', 'trade_date': '16-09-2020', 'trade_time': '15:23:17', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '1950', 'price': '137.37', 'brokerID': '4'}, {'trade_id': '1156', 'trade_date': '16-09-2020', 'trade_time': '15:23:08', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '2900', 'price': '312.18', 'brokerID': '4'}, {'trade_id': '1148', 'trade_date': '16-09-2020', 'trade_time': '15:22:55', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2450', 'price': '181.82', 'brokerID': '3'}, {'trade_id': '1144', 'trade_date': '16-09-2020', 'trade_time': '15:22:50', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'FUTURES', 'trade_action': 'SELL', 'quantity': '4150', 'price': '147.59', 'brokerID': '5'}, {'trade_id': '1142', 'trade_date': '16-09-2020', 'trade_time': '15:22:47', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '4150', 'price': '110.25', 'brokerID': '4'}, {'trade_id': '1141', 'trade_date': '16-09-2020', 'trade_time': '15:22:46', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2600', 'price': '155.39', 'brokerID': '5'}, {'trade_id': '1140', 'trade_date': '16-09-2020', 'trade_time': '15:22:44', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '2900', 'price': '280.99', 'brokerID': '2'}, {'trade_id': '1139', 'trade_date': '16-09-2020', 'trade_time': '15:22:43', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '4450', 'price': '89.66', 'brokerID': '3'}, {'trade_id': '1138', 'trade_date': '16-09-2020', 'trade_time': '15:22:41', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '4750', 'price': '44.86', 'brokerID': '3'}, {'trade_id': '1136', 'trade_date': '16-09-2020', 'trade_time': '15:22:39', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4050', 'price': '138.70', 'brokerID': '3'}, {'trade_id': '1134', 'trade_date': '16-09-2020', 'trade_time': '15:22:37', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'FUTURES', 'trade_action': 'SELL', 'quantity': '3950', 'price': '143.44', 'brokerID': '5'}, {'trade_id': '1133', 'trade_date': '16-09-2020', 'trade_time': '15:22:35', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '3150', 'price': '281.62', 'brokerID': '4'}, {'trade_id': '1131', 'trade_date': '16-09-2020', 'trade_time': '15:22:32', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '3150', 'price': '326.85', 'brokerID': '3'}, {'trade_id': '1130', 'trade_date': '16-09-2020', 'trade_time': '15:22:31', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'FUTURES', 'trade_action': 'SELL', 'quantity': '1800', 'price': '74.94', 'brokerID': '5'}, {'trade_id': '1128', 'trade_date': '16-09-2020', 'trade_time': '15:22:29', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2600', 'price': '51.63', 'brokerID': '1'}, {'trade_id': '1126', 'trade_date': '16-09-2020', 'trade_time': '15:22:26', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2600', 'price': '84.06', 'brokerID': '2'}, {'trade_id': '1121', 'trade_date': '16-09-2020', 'trade_time': '15:22:19', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '2300', 'price': '331.55', 'brokerID': '2'}, {'trade_id': '1115', 'trade_date': '16-09-2020', 'trade_time': '15:22:11', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '3750', 'price': '323.39', 'brokerID': '4'}, {'trade_id': '1109', 'trade_date': '16-09-2020', 'trade_time': '15:22:02', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '2600', 'price': '105.49', 'brokerID': '2'}, {'trade_id': '1106', 'trade_date': '16-09-2020', 'trade_time': '15:21:58', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3900', 'price': '160.32', 'brokerID': '3'}, {'trade_id': '1103', 'trade_date': '16-09-2020', 'trade_time': '15:21:53', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '3950', 'price': '44.67', 'brokerID': '2'}, {'trade_id': '1101', 'trade_date': '16-09-2020', 'trade_time': '15:21:51', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'FUTURES', 'trade_action': 'SELL', 'quantity': '3950', 'price': '73.52', 'brokerID': '2'}, {'trade_id': '1099', 'trade_date': '16-09-2020', 'trade_time': '15:21:47', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4000', 'price': '305.20', 'brokerID': '2'}, {'trade_id': '1092', 'trade_date': '16-09-2020', 'trade_time': '15:21:37', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '1900', 'price': '137.92', 'brokerID': '1'}, {'trade_id': '1091', 'trade_date': '16-09-2020', 'trade_time': '15:21:35', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '3900', 'price': '92.75', 'brokerID': '3'}, {'trade_id': '1088', 'trade_date': '16-09-2020', 'trade_time': '15:21:31', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2000', 'price': '141.92', 'brokerID': '2'}, {'trade_id': '1083', 'trade_date': '16-09-2020', 'trade_time': '15:21:23', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'FUTURES', 'trade_action': 'SELL', 'quantity': '4500', 'price': '287.74', 'brokerID': '4'}, {'trade_id': '1081', 'trade_date': '16-09-2020', 'trade_time': '15:21:20', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '4500', 'price': '252.56', 'brokerID': '2'}, {'trade_id': '1080', 'trade_date': '16-09-2020', 'trade_time': '15:21:19', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '1750', 'price': '239.02', 'brokerID': '5'}, {'trade_id': '1079', 'trade_date': '16-09-2020', 'trade_time': '15:21:18', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '3050', 'price': '232.22', 'brokerID': '2'}, {'trade_id': '1073', 'trade_date': '16-09-2020', 'trade_time': '15:21:06', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '1900', 'price': '100.37', 'brokerID': '2'}, {'trade_id': '1072', 'trade_date': '16-09-2020', 'trade_time': '15:21:05', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'FUTURES', 'trade_action': 'SELL', 'quantity': '350', 'price': '122.47', 'brokerID': '2'}, {'trade_id': '1067', 'trade_date': '16-09-2020', 'trade_time': '15:20:58', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4450', 'price': '119.06', 'brokerID': '3'}, {'trade_id': '1063', 'trade_date': '16-09-2020', 'trade_time': '15:20:52', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'FUTURES', 'trade_action': 'SELL', 'quantity': '2100', 'price': '257.94', 'brokerID': '2'}, {'trade_id': '1062', 'trade_date': '16-09-2020', 'trade_time': '15:20:51', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '1400', 'price': '93.09', 'brokerID': '4'}, {'trade_id': '1056', 'trade_date': '16-09-2020', 'trade_time': '15:20:42', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '3150', 'price': '100.19', 'brokerID': '4'}, {'trade_id': '1055', 'trade_date': '16-09-2020', 'trade_time': '15:20:40', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '4150', 'price': '113.88', 'brokerID': '1'}, {'trade_id': '1053', 'trade_date': '16-09-2020', 'trade_time': '15:20:37', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4600', 'price': '298.15', 'brokerID': '5'}, {'trade_id': '1043', 'trade_date': '16-09-2020', 'trade_time': '15:20:21', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '4500', 'price': '311.20', 'brokerID': '3'}, {'trade_id': '1037', 'trade_date': '16-09-2020', 'trade_time': '15:20:12', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '250', 'price': '326.04', 'brokerID': '3'}, {'trade_id': '1032', 'trade_date': '16-09-2020', 'trade_time': '15:20:06', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '550', 'price': '326.18', 'brokerID': '2'}, {'trade_id': '1030', 'trade_date': '16-09-2020', 'trade_time': '15:20:03', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3300', 'price': '114.97', 'brokerID': '2'}, {'trade_id': '1015', 'trade_date': '16-09-2020', 'trade_time': '15:19:39', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2350', 'price': '322.94', 'brokerID': '3'}, {'trade_id': '1014', 'trade_date': '16-09-2020', 'trade_time': '15:19:38', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '4600', 'price': '314.56', 'brokerID': '3'}, {'trade_id': '1004', 'trade_date': '16-09-2020', 'trade_time': '15:19:22', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'FUTURES', 'trade_action': 'BUY', 'quantity': '2350', 'price': '127.34', 'brokerID': '1'}, {'trade_id': '1003', 'trade_date': '16-09-2020', 'trade_time': '15:19:20', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'CALL OPTION', 'trade_action': 'SELL', 'quantity': '4100', 'price': '133.42', 'brokerID': '4'}, {'trade_id': '1002', 'trade_date': '16-09-2020', 'trade_time': '15:19:18', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'CALL OPTION', 'trade_action': 'BUY', 'quantity': '4850', 'price': '278.67', 'brokerID': '1'}]


firmDict = dict()

"""
input : checkDate (str), firmList : (list of dictionaries)
function : create a segregated dictionary from 
output : mainMap : dictionary (recursive)
"""
def generateMap(checkDate, firmTradeList):

	mainMap = {"SELL" : dict(), "BUY" : dict()}
	
	for firmTrade in firmTradeList:
	
		firmDict[firmTrade["trade_id"]] = firmTrade["securityType"]
	
		if(firmTrade["trade_date"] == checkDate):
	
			if(firmTrade["trade_action"] == "SELL"):
			
				tempDict = mainMap["SELL"] 
				
			else:
			
				tempDict = mainMap["BUY"]
			
			date = list(map(int,firmTrade["trade_date"].split("-")))
			
			time = list(map(int,firmTrade["trade_time"].split(":")))
			
			
			timeStamp = datetime(year = date[2], month = date[1], day = date[0], hour = time[0], minute = time[1], second = time[2])
			
			
			tempTuple = tuple([firmTrade["trade_id"], timeStamp])
			
			if(firmTrade["stockSymbol"] in tempDict):
			
				tempDict[firmTrade["stockSymbol"]].append(tempTuple)
				
			else:
			
				tempDict[firmTrade["stockSymbol"]] = [tempTuple]
	

	
	return mainMap
	


"""
"""
def findBuy(mainMap, custTrade, typeToFind):

	stockSymbol = custTrade["stockSymbol"]
	
	date = custTrade["trade_date"]
	
	if(date not in mainMap):
	
		return None
	
	tempDict = mainMap[date]["BUY"]
		
	if(stockSymbol not in tempDict):
		
		return None

	tempList = tempDict[stockSymbol]

	date = list(map(int,custTrade["trade_date"].split("-")))
		
	time = list(map(int,custTrade["trade_time"].split(":")))
		
	custTimeStamp = datetime(year = date[2], month = date[1], day = date[0], hour = time[0], minute = time[1], second = time[2])

	if(typeToFind == "BBS"): 
		
		if(tempList[-1][1] < custTimeStamp):
		
			tradeId = tempList[-1][0]
		
			tempList.pop()
		
			return tradeId
			
		return None

	else:
	
		ans = tuple([None])
	
		if(custTimeStamp > tempList[0][1]):
		
			return None
	
		iterator = 0
	
		for iterator in range(len(tempList)):
		
			if(tempList[iterator][1] > custTimeStamp):
			
				ans = tempList[iterator]
				
			else:
			
				break
				
		tempList.pop(iterator)
				
		return ans[0]
	
		


"""
"""
def findSell(mainMap, custTrade, typeToFind):

	stockSymbol = custTrade["stockSymbol"]
	
	date = custTrade["trade_date"]
	
	if(date not in mainMap):
	
		return None
	
	tempDict = mainMap[date]["SELL"]
		
	if(stockSymbol not in tempDict):
		
		return None			
		
	tempList = tempDict[stockSymbol]

	date = list(map(int,custTrade["trade_date"].split("-")))
		
	time = list(map(int,custTrade["trade_time"].split(":")))
		
	custTimeStamp = datetime(year = date[2], month = date[1], day = date[0], hour = time[0], minute = time[1], second = time[2])


	if(typeToFind == "SSB"):
		
		
		if(tempList[-1][1] < custTimeStamp):
		
			tradeId = tempList[-1][0]
		
			tempList.pop()
		
			return tradeId
			
		return None
		
	else:
	
		ans = tuple([None])
	
		if(custTimeStamp > tempList[0][1]):
		
			return None
	
		iterator = 0
	
		for iterator in range(len(tempList)):
		
			if(tempList[iterator][1] > custTimeStamp):
			
				ans = tempList[iterator]
				
			else:
			
				break
				
		tempList.pop(iterator)
				
		return ans[0]			
			
			
			


"""
input : mainMap dictionary (recursive), potentialList list of dictionaries
function : 
output : None
"""
def detectFraud(mainMap, potentialList):

	potentialList = sorted(potentialList, key = lambda x : datetime(year = int(x["trade_date"].split("-")[2]), month = int(x["trade_date"].split("-")[1]), day = int(x["trade_date"].split("-")[0]), hour = int(x["trade_time"].split(":")[0]), minute = int(x["trade_time"].split(":")[1]), second = int(x["trade_time"].split(":")[2])))
	
	
	for custTrade in potentialList:
	
		if(custTrade["trade_action"] == "SELL"):
		
			sellTradeId = findSell(mainMap, custTrade, "SSB")
		
			if(sellTradeId):
			
				buyTradeId = findBuy(mainMap, custTrade, "SSB")
				
				if(buyTradeId):
				
					if(firmDict[buyTradeId] == firmDict[sellTradeId]):
				
						print("\n::FRONT RUNNING DETECTED (SSB) ::\nFirm Sell : {0}\tCust Sell : {1}\tFirm Buy : {2}\n\n".format(sellTradeId,custTrade["trade_id"],buyTradeId))
						print(firmDict[buyTradeId])
						print(firmDict[sellTradeId])
				
				
		else:
		
			buyTradeId = findBuy(mainMap, custTrade, "BBS")
			
			if(buyTradeId):
			
				sellTradeId = findSell(mainMap, custTrade, "BBS")
				
				if(sellTradeId):
				
					if(firmDict[buyTradeId] == firmDict[sellTradeId]):
				
						print("\n::FRONT RUNNING DETECTED (BBS) ::\nFirm Buy : {0}\tCust Buy : {1}\tFirm Sell : {2}\n\n".format(buyTradeId,custTrade["trade_id"],sellTradeId))
						print(firmDict[buyTradeId])
						print(firmDict[sellTradeId])


"""
input : firmList : (list of dictionaries)
function : 
output : 
"""
def findUniqueDates(firmTradeList):

	dateSet = set()

	for tempDict in firmTradeList:
	
		dateSet.add(tempDict["trade_date"])
		
	return list(dateSet)


"""
input : listOfDates (list of unique dates), firmList : (list of dictionaries)

"""
def generateDateMainMap(listOfDates, firmTradeList):

	mainMap = dict()
	
	for date in listOfDates:

		mainMap[date] = generateMap(date, firmTradeList)
		
	return mainMap

		
#MAIN


listOfDates = findUniqueDates(firmTradeList)

mainMap = generateDateMainMap(listOfDates, firmTradeList)

#print(firmDict)
#print(mainMap)

detectFraud(mainMap, potentialList)


