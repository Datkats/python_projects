def convertpigLatin():
    print("Enter a sentence and I'll convert to piglatin")
    sentence=input("Sentence: ")                  # get input
    sentence=sentence.split()                     # split into words
    newsentence=""                                # create empty string
    for word in sentence:                         # loop through the user sentence words
        newsentence+=word[1:]+word[:1]+"ay"+" "   # concatenate words(from second letter till the end, first letter of the word and word "ay")
    print(newsentence)
convertpigLatin()
