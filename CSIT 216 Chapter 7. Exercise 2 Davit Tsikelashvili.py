import random#import random module
lottery_numbers=[]# create empty list
for n in range(7):#create loop
    random_number=random.randint(0,9)# create random number
    lottery_numbers.append(random_number)# add that random number to a list
print("Here is your lottery numbers")
for n in lottery_numbers:# loop the list and print its items
    print(n)
