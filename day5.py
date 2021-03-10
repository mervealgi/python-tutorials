#INTRODUCTION TO PYTHON DAY5

#????? USE input INSTEAD OF raw_input

###ZIP 

list1 = [1,2,3]
list2 = [4,5,6]

list3 = [a + b for a,b in zip(list1,list2)]
print(list3)  #output will be [5, 7, 9]


