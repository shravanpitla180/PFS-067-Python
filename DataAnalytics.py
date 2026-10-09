#Introduction to Data Analytics:-

# It is a process of collecting, cleaning, transforming, analyzing, and interpreting data to find 
# useful info and make decisions.

# Important Steps:-
# 1.Data collection:
# Excel, CSV, Databases, APIs, Websites, Applications

# 2.Data Cleaning:-
# Missing values, Duplicate records, Incorrect values, Wrong formats.

# 3.Data processing:-
# Converts the data into useful format.

# 4.Data Analysis
# Finding patterns and relationships

#5.Visualization:-
# Representing data using bar, line, pie, histograms.

# Numpy = Numerical Pyhton
# It is a Pyhton library used for numerical calculations, working with arrays,
# mathematical operations, matrix operations.

import numpy as np
marks = np.array([
    [81, 82, 88],
    [83, 78, 68],
    [77, 81, 80]
    ])
print(marks)
print(marks.ndim)
print(marks.shape)
print(marks.size)
print(marks.dtype)
print(marks[0][0])
print(marks[0][1])
print(marks[0][2])
print(marks[1][0])
print(marks[1][1])
print(marks[1][2])
print(marks[2][0])
print(marks[2][1])
print(marks[2][2])
print(marks[0:2, 1:3])
# [0:2] --> rows 0 and 1
# [1:3] --> columns 1 and 2
# [0, 1] [0, 2] [1, 1] [1, 2]

#Crating Special Arrays
# 1.np.zeros() - Creates an array filled with zeros.

import numpy as np
a = np.zeros(5)
print(a)

b = np.zeros((2, 3))
print(b)

#2.np.ones --> fills with value 1
import numpy as np
a = np.ones(5)
print(a)

b = np.ones((2, 3))
print(b)

#3.np.arange()
#Similar to Python range
import numpy as np
a = np.arange(1, 10)
print(a)

# Array Operations

import numpy as np
a = np.array([40, 25, 30])
b = np.array([20, 5, 15])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#Comparsion Operator

import numpy as np
a = np.array([10, 20, 40, 50])
print(a > 20)
print(a[a > 20])

#Mathematical Functions
import numpy as np
marks = np.array([70, 75, 85, 82, 90])
#sum
print(np.sum(marks))
#Average
print(np.mean(marks))
#maximum
print(np.max(marks))
#Minimum
print(np.min(marks))


import numpy as np
marks = np.array([
    [81, 82, 88],
    [83, 78, 68],
    [77, 81, 80]
    ])
#Column wise
print(np.sum(marks, axis = 0))
#Row wise
print(np.sum(marks, axis = 1))

#Reshaping array
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print(b)