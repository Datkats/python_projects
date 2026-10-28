def celsius_to_f():# creating the function
    celsius=int(input("Enter the celsius: "))# asking celsius to user
    farenheit=9/5*celsius+32 #calculates farenheit based on the user's input
    print(f"{celsius} celsius is {int(farenheit)}farenheit") #displays the result and converts farenheit into integer
celsius_to_f() #calling the function
