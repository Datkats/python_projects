import random

def write_random_numbers():
    count = int(input("How many random numbers should the file hold? "))# get input from user of how many random numbers to generate

    # Open a file for writing
    with open("random_numbers.txt", "w") as f:# open,write, and close the file
        for _ in range(count):
            number = random.randint(1, 500)  # create random number between 1 and 500
            f.write(str(number) + " ")       # write number to file separated by spaces

    print(f"{count} random numbers have been written to numbers.txt.")

if __name__ == "__main__":
    write_random_numbers()
