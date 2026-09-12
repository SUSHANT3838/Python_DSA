"""
Slicing
str = "My name is Suhant"
str[start:stop:step]
start include but stop exclude while printing slice
"""

str = "Hello world"
# positive indices
print(str[:4]) # start to 4th element excluding 4th
print(str[2:]) # start from 2 up to end
print(str[1:9:2]) # start from 1 end to 4 by steping 2 
# negative indices
# helps to print the element when length is unknow
print(str[:-3]) 
print(str[::-1]) # revers the string

"""
we use the slice() function to achieve the same slicing
slice(start, stop, step)
"""
str = "Hello, world"
print(str[slice(1,4)])