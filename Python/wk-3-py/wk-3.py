hungry = False
if hungry :
    print("eat")
else :
    print("do not eat")
    
# if elif else
"""If grade is 90 or higher, print "A"
Else if grade is 80 or higher, print "B"
Else if grade is 70 or higher, print "C"
Else if grade is 60 or higher, print "D"
Else, print "F" """

grade = 85
if grade >= 90 :
    print("A")
elif grade >= 80 :
    print("B")
elif grade >= 70 :
    print("C")
elif grade >= 60 :
    print("D")
else :
    print("F")
    
grades = [90, 85, 70, 60, 45]
for grade in grades :
    print(grade)
    if grade >= 90 :
        print("A")
    elif grade >= 80 :
        print("B")
    elif grade >= 70 :
        print("C")
    elif grade >= 60 :
        print("D")
    else :
        print("F")
        
for grade in grades:
    if grade > 95:
        print("Exceeding expectations")
    elif grade >= 80:
        print("Approaching expectations")
    elif grade >= 70:
        print("Meets expectations")
    elif grade >= 60:
        print("You can do better")
    else:
        print("Put more effort")
        
grades.extend([50, 81, 50])
print(grades)

passed_grades = [grade for grade in grades if grade >= 70]
print(passed_grades)

# lambda function

failed_grades = list(map (lambda grade: grade < 69, grades))
print(failed_grades)

# Coding Challenges for basic control flows and functions

"""
1. Large Power

Create a method that tests whether the result of taking the power of one number to another number 
provides an answer which is greater than 5000. 
We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. 
In order to accomplish this, we will need the following steps:

Define the function to accept two input parameters called base and exponent
Calculate the result of base to the power of exponent
Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False


Coding Question

Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False
"""

def large_power(base, exponent):
    result = base ** exponent
    print(result)
    if result > 5000:
        return True
    else:
        return False
    
print(large_power(2, 13)) # True
print(large_power(2, 12)) # False
print(large_power(10, 3)) # False
print(large_power(10, 4)) # True
print(large_power(7, 4)) # True


"""
2.Divisible By Ten

Create a function that determines whether or not a number is divisible by ten.
A number is divisible by ten if the remainder of the number divided by 10 is 0. 
Using this, we can complete this function in a few steps:

Define the function header to accept one input num
Calculate the remainder of the input divided by 10 (use modulus)
Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False




Coding question

Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. 
Consider using modulo operator % to check for divisibility.
"""

def divisible_by_ten(num):
    if num % 10 == 0:
        print(num)
        return True
    else:
        return False
    
print(divisible_by_ten(20)) # True
print(divisible_by_ten(25)) # False
print(divisible_by_ten(0)) # True
print(divisible_by_ten(-10)) # True
print(divisible_by_ten(-5)) # False