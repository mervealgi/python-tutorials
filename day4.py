#INTRODUCTION TO PYTHON DAY4

###IF ELSE

###
country = "Portugal"
user_input = raw_input("Please enter a character: ")

if user_input in country:
    print("Exist!")
else:
    print("Dont exist!")

###
num = int(input("Please enter a number:"))
if num < 0:
    num *= -1 
print("Result: ",num)

###
score = int(input("Please enter yout score: "))

if score <= 50:
    print("Not pass, try again")
elif score <= 70:
    print("Pass but not excellent.")
elif score <= 100:
    print("Excellent")


###
mid_exam = int(input("Please enter your mid exam result: "))
fin_exam = int(input("Please enter your finale exam result: "))

if(mid_exam <= 50 and fin_exam <= 50):
    print("You ve failed :(")
elif(mid_exam >= 50 and fin_exam >= 50):
    print("You ve passed :)")


### WHILE

number = 0

while number < 9:
    print("Value:{}".format(num))
    number = number +1   #infinite loop




