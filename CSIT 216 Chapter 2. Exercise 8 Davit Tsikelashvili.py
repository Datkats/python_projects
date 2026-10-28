# asking user the price for the food
meal_price=float(input("Enter the charge for the food: "))
while meal_price<=0:# check if user typed correct input, if not ask again
    print("Please enter correct amount")
    meal_price=float(input("Enter the charge for the food: "))
# calculation of tip, tax, and total
tip=0.18*meal_price
sales_tax=0.07*meal_price
total=meal_price+tip+sales_tax
#displays the amount of tip, tax, and total
print(f"Your amount of tip of 18 percent is: ${tip:.2f}")
print(f"Your amount of sales tax of 7 percent is: ${sales_tax:.2f}")
print(f"Your total amount is: ${total:.2f}")
