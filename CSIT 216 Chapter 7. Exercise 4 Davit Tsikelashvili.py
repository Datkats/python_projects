def main():
    numbers=get_list()# call get_list function and assign it to numbers variable
    total=get_total(numbers)# call get_total function, give numbers as an argument and assign it to total variable
    average=get_average(numbers,total)#call get_average function, give numbers and total as a argument and assign it to average variable
    print(f"Here is the smallest number in the list:{min(numbers)}")
    print(f"Here is the highest number in the list:{max(numbers)}")
    print(f"Here is your total of the numbers in the list:{total:.2f}")
    print(f"Here is the average of the numbers in the list:{average:.2f}")
def get_list():# get numbers of list
    numbers=[0]*20# create list with 20 items
    print("Lets enter series of 20 numbers")
    for n in range(len(numbers)):# create a loop in the range of the length of the list
        numbers[n]=float(input(f"{n+1}: "))# get input and assign it to list with index n
    return numbers #return list
def get_total(value_list):# create function that gets total
    total=0 # set accumulator
    for n in range(len(value_list)):# create a loop in the range of the length of the list
        total+=value_list[n] # add list's index n to total
    return total # return total
def get_average(value_list,total):# create a function that calculates average. function gets two argument: list and total
    average=total/len(value_list) # calculates average
    return average # return average
if __name__=="__main__":
    main()
