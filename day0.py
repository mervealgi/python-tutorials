#INTRODUCTION TO PYTHON DAY0

print("Hello World")

var1 = "Hello"
var2 = "World"

#print("variable1 :" , var1) 
print("My name is {}" .format(var2))


###VARIABLES 

#INTEGER

var_int = 5
print(var_int)


var_integer = 3.00
print(type(var_integer)) #output will be float

#STRING

var_string = "Hello"
print(var_string)
print("Hello")

print(type(var_string))  #print data types with its class


#FLOAT
var_float = 3.18
print(type(var_float))  #if . -> , type would be TUPLE

#BOOLEAN

var_boolean1 , var_boolean2 = True , False
print(type(var_boolean1))
print(var_boolean2)


#COMPLEX
#DICTIONARY
#TUPLE
#SET


###SWAPPING

data1 = 6
data2 = 45
data3 = 2
data4 = 78

print(data1, data2, data3, data4)
data1, data2, data3, data4 = data4, data3, data2, data1

print(data1, data2, data3, data4)

###LEN

var_len = len("Python")
print(var_len)      #same usage with above

print(len("Python"))

##F-STRING

var_string2 = "Portugal"
