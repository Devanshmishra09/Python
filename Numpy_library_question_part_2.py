# Question 4: How do you reshape data from a 1D array to a 2D matrix?

import numpy as np

# A flat 1D array of 6 elements
data_1d = np.array([10, 20, 30, 40, 50, 60])

# Reshape into 3 rows and 2 columns
data_2d = data_1d.reshape(3, 2)

print("Original 1D shape:", data_1d.shape)
print("Reshaped 2D Matrix:\n", data_2d)
print("New 2D shape:", data_2d.shape)



# Question 5: How do you extract specific columns or rows from a 2D dataset (Slicing)?

import numpy as np

# Dataset matrix: [Age, Income] for 3 individuals
dataset = np.array([
    [25, 45000],
    [32, 60000],
    [47, 85000]
])

# Extract the entire second column (Income) -> using [row_slice, column_slice]
# ':' means all rows, '1' means index 1 (the second column)
income_column = dataset[:, 1]

# Extract the first row completely (First person's data)
first_person = dataset[0, :]

print("Income Column Only:", income_column)
print("First Person Data:", first_person)


