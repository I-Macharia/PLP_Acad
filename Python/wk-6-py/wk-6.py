# Python Libraries

#NumPy

import numpy as np

# Create a NumPy array with number 10 to 50
arr = np.arange(10, 51)
print("Array:", arr)
print()

# Get the Max value
max_arr = np.max(arr)
print("Max:", max_arr)
print()

# Get the Min value
min_arr = np.min(arr)
print("Min:", min_arr)
print()

# Multiply all elements by 3
multiplied_arr = arr * 3
print("Multiplied Array:", multiplied_arr)


# Pandas

import pandas as pd 

# Create a DataFrame with three students name, age and grade

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 19],
    'Grade': [65, 50, 88]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# add new column
df['Passed'] = df['Grade'] > 50
print("\nUpdated DataFrame:")
print(df)

# filter only passed students
passed_students = df[df['Passed']]
print("\nPassed Students:")
print(passed_students)
print()


# Matplotlib

import matplotlib.pyplot as plt

# Create a bar chart of 5 different countries and their population

data = {
    'Country': ['Kenya', 'Tanzania', 'Uganda', 'Rwanda', 'Burundi'],
    'Population (Millions)': [53.77, 61.50, 45.71, 12.63, 11.86]
}

df_population = pd.DataFrame(data)
print("Population DataFrame:")
print()
print(df_population)
print()

# Plotting the bar chart
plt.bar(df_population['Country'], df_population['Population (Millions)'], color='skyblue')
plt.title('Population of East African Countries')
plt.xlabel('Country')
plt.ylabel('Population (Millions)')
plt.xticks(rotation=45)
plt.show()


# Plotting a pie chart
# Create a pie chart showing how a student spends 24 hours of their day.
labels = ['Sleeping', 'Studying', 'Eating', 'Leisure', 'Other']
times = [8, 6, 2, 4, 4]

plt.pie(times, labels=labels, autopct='%1.1f%%')
plt.title('Student Daily Activities')
plt.show()

# Plotting a line chart
# Make a line chart that shows temperature changes during the day (morning, noon, evening, night).
x = ['Morning', 'Noon', 'Evening', 'Night']
y = [15, 25, 20, 10]

plt.plot(x,y)
plt.title('Temperature Changes During the Day')
plt.xlabel('Time of Day')
plt.ylabel('Temperature (°C)')
plt.show()