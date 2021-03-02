#INTRODUCTION TO PYTHON DAY3

###INPUT #????? USE input INSTEAD OF raw_input

#input1 = raw_input("Please enter your favourite city: ") #must be string 
#print(input1)
#print(type(input1))

#input2 = int(raw_input("Please enter an integer: ")) #turn to integer
#print(input2) #can not be entered float
#print(type(input2))



months = 12
days = 365
print("1 year is " + str(months) + " months and " + str(days) + " days." )


###LISTS

#LIST 1
user_list1 = [1,2,3,4,5,6]

print(user_list1)
print(type(user_list1)) #list

print(user_list1[0]) #1
print(user_list1[5]) #6
print(user_list1[-1]) #6

user_list1[1] = "python" #change the list line with it 
print(user_list1)

user_list1.append("deep") #add item to end of list 
print(user_list1)

user_list1.append("learning")
print(user_list1)

user_list1.pop() #remove the last item
print(user_list1)

user_list1.remove(5) #[1, 'python', 3, 4, 6, 'deep']
print(user_list1)

print(user_list1.index(1)) #output will be 0

print(user_list1.count("deep")) #count to item "deep"


#LIST 2

user_list2 = [54,12,45,76,9]

user_list2.sort()
print(user_list2)

user_list2.reverse()
print(user_list2)


#LIST 3

user_list3 = ["python" , "machine", "deep" ,"learning"]

user_list3.sort() #order with alphabetically
print(user_list3)

user_list3.extend(user_list2) #combined two lists
print(user_list3)


#LIST 4

listception = ["python", "Java", 3.2 ,4 ,11, [5,65,7,8,9]]
print(listception[-1]) #output will be the last item : [5, 65, 7, 8, 9]

listception.insert(4,"fourfor")
print(listception)


###RANGE

list_range = list(range(0,15,2))
print(list_range) #output will be [0, 2, 4, 6, 8, 10, 12, 14]

print(6 in list_range) #True

