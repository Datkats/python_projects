def average_calc():# create a function
    with open("numbers.txt","r") as f: #open, read, and close the file
        contents=f.read()# read the file
        numbers=contents.split()# split the numbers into seperate numbers bc it is one big long string and assign to a variable numbers
        count=0# to count the amount of numbers
        total=0# to count the sum of the numbers
        for number_in_str in numbers: # loop through the numbers which is as a string
            number=int(number_in_str)# convert the strgin numbers into integers
            count+=1# keep counting of the amount of numbers
            total+=number# keep counting of sum of numbers
        average=total/count if count != 0 else 0# if in the file there was no numbers average will be 0 if not calculate average
        return average #return average

if __name__=='__main__':
    print(average_calc())# call and print the funtion
