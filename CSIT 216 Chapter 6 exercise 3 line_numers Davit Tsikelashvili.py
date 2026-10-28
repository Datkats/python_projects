def display_file_with_line_numbers():# create function
    filename = input("Enter the name of the file: ")#get name of the file

    # Automatically add .txt if the user didn't include an extension
    if not filename.endswith(".txt"):# add .txt if user didn't include in the name
        filename += ".txt"

    try:
        with open(filename, 'r') as file:# open, read and close the file
            for line_number, line in enumerate(file, start=1):#loop through the file by the following index which starts from one
                print(f"{line_number}: {line.rstrip()}")# print index and item from the file
    except FileNotFoundError:# if user typed incorrect file name print that couldn't found
        print(f"Error: The file '{filename}' was not found.")
        
if __name__=='__main__':
    display_file_with_line_numbers()
