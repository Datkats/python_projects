def get_scores():
    scores_list=[]                #create empty list
    for n in range(1,6):          # ask score six times
        scores=float(input(f"Enter test score: student{n}: "))
        while not 0<=scores<=100: # input validation check. if user typed invalid number, ask again
            print("Please enter valid score (it must be in range:0-100)")
            scores=float(input(f"Enter test score: student{n}: "))# ask again until it is valid number
        scores_list.append(scores)# add score in the empty list
    return scores_list            # return list
def calc_average(number_list):
    total=0
    for number in number_list:
        total+=number             # calculate total 
    average=total/len(number_list)# calculate average->Divide the total by the amount of numbers in the list
    return average                #return average
def determine_grade(scores):
    for i,score in enumerate(scores,start=1): #loop through test scores and keep index and print their appropriate grade
        if 90<=score<=100:
            print(f"grade of student{i}:A")
        elif 80<=score<90:
            print(f"grade of student{i}:B")
        elif 70<=score<80:
            print(f"grade of student{i}:C")
        elif 60<=score<70:
            print(f"grade of student{i}:D")
        elif score<60:
            print(f"grade of student{i}:F")
def main():
    scores=get_scores()# get_scores function assign to scores variable
    determine_grade(scores)# calling the determine_grade function and give scores variable(Inside user's input) as an argument
    print(f"average test score is {calc_average(scores)}")# call calc_average function and give scores variable(Inside user's input) as an argument
main()
