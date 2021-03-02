#INTRODUCTION TO PYTHON DAY2

###LOGICAL OPERATIONS 

a, b = True , False
print(type(a))

print(a or b) #will be True
print(a and b) #will be False
print(not a) #will be False
print (a != b) #will be True,bcs re not equal
print(a == b) #will be False, bcs re not equal



###SLICING 


array1 = "PYTHON"

print(array1[0]) #P
print(array1[3]) #H

print(array1[-1]) #N
print(array1[-4]) #T

print(array1[:]) #will print all #PYTHON

print(array1[0:6]) #will print from 0 to 5th but not 6th
print(array1[1:3]) #YT

print(array1[0:]) #from 0 to all 
print(array1[4:]) #ON

print(array1[:3]) #from begin to 3th but not 3th #PYT
print(array1[:6]) #PYTHON

print(array1[::-1]) #NOHTYP

city = "Porto"
print(city[0:5:1]) #start:end:step #Porto
print(city[1:5:2]) # o t
print(city[0:5:2]) #P r o

print("t" in city) #will be True
print("p" in city) #will be False bcs we have upper P

print("or" in city) #will be True 
print("po" in city) #will be False bcs we have upper Po

ai = "artificial" + " " + "intelligence"
print(ai)

###LETTERS 

word1 = "machine learning"
print(word1.capitalize()) #Machine learning

print(word1.upper()) #MACHINE LEARNING

print(word1.replace("machine","deep")) #deep learning

print(word1.strip()) #????????????




