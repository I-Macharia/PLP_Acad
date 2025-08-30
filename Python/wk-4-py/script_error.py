# Week 4 Assignment


"""
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
Outcomes 🎉

"""

def read_write():
    
    # ask user for file name
    input_file = input("Enter the input file name (with path if not in current directory): ")
    print(input_file)
    try: 
        # open the file
        with open(input_file, "r") as infile:
            data = infile.read()
            print(data)
            infile.close()

        # Modify the data
        modified_data = data+ "\n The word count in this file is:" + str(len(data.split()))
        print(modified_data)

        # Save the new file
        with open("saved.txt", "w") as save:
            save.write(modified_data)
            print("Data written to saved.txt")
        
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    
# run the function

read_write()
