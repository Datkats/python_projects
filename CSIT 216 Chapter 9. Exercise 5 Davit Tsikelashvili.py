import pickle

def main():
    try:
        with open("ipsum.txt", 'r') as infile: # Open the file as read  mode
            text = infile.read()# read the file and assign it to the text variable
        words = text.lower().split()# Convert text to lowercase and split into words

        # Create dictionary for word frequencies
        word_count = {}

        for word in words: # loop through words
            word = word.strip('.,!?":;()[]{}')# Remove punctuation around words
            if word:# if that word exists and it's not just empty it will be true
                word_count[word] = word_count.get(word, 0) + 1 # gets the value for the key, if it couldn't find it returns 0, and adds 1,stores the new number back into the dictionary (creating or updating the key)

        # pickling
        with open('word_frequencies.pkl', 'wb') as pickle_file:
            pickle.dump(word_count, pickle_file)# writes a serialized (binary) version into the 

        with open('word_frequencies.pkl', 'rb') as pickle_file:# open read binary mode
            loaded_data = pickle.load(pickle_file)# unpickling
            print("\nLoaded data preview:")
            for word, count in list(loaded_data.items()):# loop through key value pair and display them
                print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name and try again.")

if __name__ == "__main__":
    main()
