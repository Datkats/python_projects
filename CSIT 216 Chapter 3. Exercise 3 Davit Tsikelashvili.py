age=int(input("Enter your age: "))# asking user the age
while age<0:# check if age is valid, if it's invalid ask again until age will be valid
    print("Please enter a correct age(it be greater than 0)")
    age=int(input("Enter your age: "))
#check the age and display either infant, child, teenager, or adult
if age<=1:
    print("You are an infant ")
elif 1<age<13:
    print("You are a child ")
elif 13<=age<20:
    print("You are a teenager ")
else:
    print("You are an adult")
