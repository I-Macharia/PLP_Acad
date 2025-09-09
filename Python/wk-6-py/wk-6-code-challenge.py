"""Challenge: Use popular Python libraries to perform useful tasks!

📌 Task Requirements:

Import the following libraries:

pandas (for data manipulation)
numpy (for numerical operations)
matplotlib (for data visualization)
requests (for making web requests)

Complete the following tasks using the libraries:

Create a NumPy array of numbers from 1 to 10 and calculate the mean.
Load a small dataset into a pandas DataFrame and display summary statistics.
Fetch data from a public API using requests and print a key piece of information.
Plot a simple line graph using matplotlib (e.g., a list of numbers).

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Task 1: Create a NumPy array of numbers from 1 to 10 and calculate the mean.
arr = np.arange(1, 11)
print("NumPy Array:", arr)
print()

mean_val = np.mean(arr)
print("Mean of the array:", mean_val)
print()

# Task 2: Load a small dataset into a pandas DataFrame and display summary statistics.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [23, 30, 22, 35, 28],
    'Score': [85, 90, 78, 88, 92]
}

# convert the data to a dataframe
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print()

# Display summary statistics
sumamry_stats = df.describe()
print("Summary Statistics:")
print(sumamry_stats)
print()


# Task 3: Fetch data from a public API using requests and print a key piece of information.
response = requests.get("https://academy.powerlearnprojectafrica.org/module/62fbec9d28ac4762bc524f92?study=true&week=63ea74fd022732bf59cec31c&lesson=67da7ca695cb05d0e0f0364a")
print("Status Code:", response.status_code)
print(response.headers)
print(response.text)
print()

# Task 4: Plot a simple line graph using matplotlib (e.g., a list of numbers).
x = np.arange(1, 11)
y = x ** 2 
plt.plot(x, y, marker='o')
plt.title("Line Graph of y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# End of code challenge