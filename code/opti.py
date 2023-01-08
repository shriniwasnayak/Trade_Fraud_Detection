l = [-1,1,-1,1,2,3,4,-4,-5]

# sum : maxele
numDict = {0:0}

altDict = dict()

for num in l:

	#print("Num",num,sep=" : ")

	#input()

	keyList = numDict.keys()

	#print("KeyList",keyList,sep=" : ")

	#input()
	
	for key in keyList:
	
		temp = 0
	
		if( (num + key) in keyList):
		
			temp = numDict[key]
			
		
		altDict[num + key] = max(temp, numDict[key] + 1)
		
	numDict = {**altDict}
	
print(numDict[0])
