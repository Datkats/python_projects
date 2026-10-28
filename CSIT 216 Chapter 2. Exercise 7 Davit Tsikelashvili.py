# asking input from user about miles and gallons
miles_driven=float(input("Enter the number of miles driven "))
gallons_used=float(input("Enter the number of gallons used "))
# check, if user typed wrong input asks again, if not it calculates and displays the MPG
while miles_driven < 0 or gallons_used <= 0:
    print("Either amount of miles or gallons is incorrect. Try again Please")
    miles_driven=float(input("Enter the number of miles driven "))
    gallons_used=float(input("Enter the number of gallons used "))
mpg=miles_driven / gallons_used
print(f"Your vehicle's MPG is {mpg:.2f}")
