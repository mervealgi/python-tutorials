#INTRODUCTION TO PYTHON DAY4

###IF ELSE #????? USE input INSTEAD OF raw_input

###
country = "Portugal"
user_input = raw_input("Please enter a character: ")

if user_input in country:
    print("Exist!")
else:
    print("Dont exist!")

###
num = int(raw_input("Please enter a number:"))
if num < 0:
    num *= -1 
print("Result: ",num)

###
score = int(raw_input("Please enter yout score: "))

if score <= 50:
    print("Not pass, try again")
elif score <= 70:
    print("Pass but not excellent.")
elif score <= 100:
    print("Excellent")


###
mid_exam = int(raw_input("Please enter your mid exam result: "))
fin_exam = int(raw_input("Please enter your finale exam result: "))

if(mid_exam <= 50 and fin_exam <= 50):
    print("You ve failed :(")
elif(mid_exam >= 50 and fin_exam >= 50):
    print("You ve passed :)")


### WHILE

number = 0

while number < 9:
    print("Value:{}".format(num))
    number = number +1   #infinite loop


### WHILE IN LISTS

list1 = [1,2,3,4,5,6,7]

i = 0
while (i < len(list1)):
    print(i, "th item: ", list1[i])
    i += 1

###

while True:
    a = raw_input("Enter a value: ")
    if a == "Exit":
        break


### FOR

list1 = [1,2,3,4,5,6,7]
for i in list1:
    print(i)

###
list2 = list(range(8))
print(list2)
squares = [i**2 for i in list2]
print(squares)

###
mylist = [1,2,3,4,5,6]
print(mylist[0])

max_num = mylist[0]

for i in mylist:
    if i > max_num:
        max_num = i
        print("Max num is: ", max_num)
        print("i: ",i)
    print(max_num)