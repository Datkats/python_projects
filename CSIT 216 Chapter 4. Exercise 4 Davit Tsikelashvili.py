mph=int(input("What is the speed of the vehicle in mph?: ")) # asking the speed
hours=int(input("How many hours has it traveled?: ")) # asking the hours of traveled
while mph<0 or hours<0: # check if inputs are valid. if they are invalid ask them again until they type valid input
    print("either speed or hours traveled is incorrect. Please try again")
    mph=int(input("What is the speed of the vehicle in mph?: ")) # asking again the speed
    hours=int(input("How many hours has it traveled?: ")) # asking again the hours of traveled
print(f"Hour {"Distance traveled":>40}")
print("___"*15)
for n in range(hours): # loop that prints the distance the vehicle has traveled for each hour of that time period
    print(f"{n+1} {mph*(n+1):>40}")
