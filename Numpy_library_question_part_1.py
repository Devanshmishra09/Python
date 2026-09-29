# Question 1: How do you calculate basic statistics (Mean, Median, Standard Deviation) for a dataset?


import numpy as np

# Sample dataset: Monthly sales numbers
sales = np.array([1200, 1500, 900, 2500, 1800, 1100, 3000])

# Calculate statistics
mean_sales = np.mean(sales)
median_sales = np.median(sales)
std_dev_sales = np.std(sales)

print("Mean Sales:", mean_sales)
print("Median Sales:", median_sales)
print("Standard Deviation:", round(std_dev_sales, 2))


# Question 2: How do you filter data based on a condition (Boolean Indexing)?

import numpy as np

# Dataset: Test scores of students
scores = np.array([55, 82, 90, 45, 76, 89, 60])

# Filter scores that are greater than or equal to 75
passing_scores = scores[scores >= 75]

print("All Scores:", scores)
print("Passing Scores (>= 75):", passing_scores)


# Question 3: How do you replace specific values in an array conditionally?

import numpy as np

# Dataset: Temperature readings (with some faulty negative values)
temperatures = np.array([22, 25, -5, 28, -1, 30])

# If temperature is less than 0, replace it with 0. Otherwise, keep it.
cleaned_temperatures = np.where(temperatures < 0, 0, temperatures)

print("Original:", temperatures)
print("Cleaned: ", cleaned_temperatures)
