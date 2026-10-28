def main():
    userstring=input("Enter any word and I'll count number of vowels and consonants: ").lower().strip()# get input
    numberVowels=countvowels(userstring)# call countvowels function and give user input as argument
    numberConsonants=countconsonants(userstring)# call countconsonants function and give user input as argument
    print(f"Your word has {numberVowels} vowels and {numberConsonants} consonants")

# create constants of vowels and consonants
VOWELS=("a","e","i","o","u")
CONSONANTS=("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")

# create countvowels function. loop through the string and count vowels
def countvowels(string):
    count=0
    for letter in string:
        if letter in VOWELS:
            count+=1
    return count

# create countvowels function. loop through the string and count consonants
def countconsonants(string):
    count=0
    for letter in string:
        if letter in CONSONANTS:
            count+=1
    return count
if __name__ == "__main__":
    main()
