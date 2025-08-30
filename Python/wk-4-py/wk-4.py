# File Handling
# opening file
file = open("/home/bobbybob/Documents/PLP_Acad/Python/wk-4-py/example.txt", "r")
# Reading file
data = file.read()
print(data)
# close the file
file.close()

# open the file in write mode
file2 = open("/home/bobbybob/Documents/PLP_Acad/Python/wk-4-py/example.txt", "w")
# Write data in the file
file2.write("File Handling Lesson")
print(data)

file2.close()

# Error Handling
try:
    with open("example.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
finally:
    file.close()