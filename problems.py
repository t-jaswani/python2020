
#Write a NumPy program to generate a random number between 0 and 1.

#bytes 
arr1 = np.array([[1,2,3],[7,8,6]])
print(arr1.nbytes)
arr2 = np.array([1,5,6,9])
print(arr2.nbytes)
arr1 = np.array([[1,2,3,4,5],[7,8,6]])
print(arr1.nbytes)
arr2 = np.array([1,5,6,9])
print(arr2.nbytes)
--------
#Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
import numpy as np
x = np.zeros((4, 4))
x[::2, 1::2] = 1
x[1::2, ::2] = 1
print(x)
--------------
Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Replace the 'qualify' column contains the values 'yes' and 'no' with T
rue and False:
attempts name qualify score
a 1 Anastasia True 12.5
b 3 Dima False 9.0
......
i 2 Kevin False 8.0
j 1 Jonas True 19.0
------------------
https://www.w3resource.com/python-exercises/pandas/index-dataframe.php
question 32 na