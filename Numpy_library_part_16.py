# Multiplication : 
#  The numpy.matmul() function computes the matrix product of two arrays.
# In modern Python, the @ operator serves as a direct, highly readable shorthand for this 
# function when applied to NumPy ndarrays

# ex 
import numpy as n 

A = n.array([[1, 2],[3, 4]])

B = n.array([[5, 6],[7, 8]])

# Using the @ operator
result = A @ B
print(result)


# Determinant :  A determinant is a special number (scalar value) 
# that can be calculated from a square matrix in linear algebra
# n.linalg.inv()   : method for determination 
# ex 
import numpy as n 
a=n.array([[1,2],[3,4]])
print(n.linalg.inv(a))


# inverse matrix :The inverse of a matrix A (denoted as A⁻¹) is a 
# special matrix that, when multiplied by the original matrix, yields the identity matrix (A × A⁻¹ = A⁻¹ × A = I

#  n.linalg.eig()  method 

import numpy as n 
a=n.array([[1,2],[4,5]])
print(n.linalg.eig(a))