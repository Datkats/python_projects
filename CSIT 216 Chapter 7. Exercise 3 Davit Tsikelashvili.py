def main():
    stats=get_statistic()# call get_statistic function and assign it to stats variable
    total=get_total(stats)# call get_total function, give stats as an argument and assign it to total variable
    average=get_average(stats,total)#call get_average function, give stats and total as a argument and assign it to average variable
    print(f"Here is your total rainfall of the year {total:.2f}")
    print(f"Here is the average monthly rainfall {average:.2f}")
    print(f"Here is the smallest amount of rainfall {min(stats)}")
    print(f"Here is the highest amount of rainfall {max(stats)}")
def get_statistic():# get rainfall statistic
    rainfall=[0]*12# create list with 12 items
    for n in range(len(rainfall)):# create a loop in the range of the length of the list
        rainfall[n]=float(input(f"Enter a total rainfall for month{n+1}: "))# get input and assign it to list with index n
    return rainfall #return list
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
