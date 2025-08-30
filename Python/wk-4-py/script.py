# Week 4 - Code Challenge
# Open the file
with open("Python/wk-4-py/input.txt", "r") as file:
    data = file.read()
    
print(data)
print()

# Count the number of words. 
word_count = len(data.split())
print("Number of words:", word_count)
print()

# Convert the entire contents to uppercase
data_uppercase = data.upper()
print(data_uppercase)

# Output the new file to output.txt
with open("Python/wk-4-py/output.txt", "w") as data:
    data.write(data_uppercase)
    print("Data written to output.txt")