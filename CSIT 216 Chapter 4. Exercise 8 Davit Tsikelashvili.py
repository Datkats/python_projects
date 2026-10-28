user_positive_number=int(input("Enter a positive number: "))# getting the input(positive number)
total=0
while user_positive_number<0:# check if user type positive number, if not ask again
    user_positive_number=int(input("Please enter a positive number: "))# asking positive number again
else:
    while user_positive_number!=-1:#using sentinel(signal the end of the series)
        total+=user_positive_number# adding positive number to total
        user_positive_number=int(input("Enter another positive number(if you want to stop this enter negative1 '-1'): "))# asking another positive number if user want to stop they can type -1
print(f"Your numbers sum is {total}")# display the total
