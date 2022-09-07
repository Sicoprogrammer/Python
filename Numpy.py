'''Creating numpy 2D array'''
import numpy as np
my = np.array([[1, 2, 56, 65, 45, 54, 99]], np.int32)
print(my)
print(my[0, 5])

#Shape of the array
print(my.shape)
print(my.dtype)
#Change of the number in the list
my[0, 1] = 490
print(my)
#Dimentional
list = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(list)
print(list.size)
#Range
a = np.arange(20)
print(a)#(n-1)
#Equal linear space
lnip = np.linspace(1, 5, 10)
