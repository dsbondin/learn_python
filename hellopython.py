import random
import sys
import os

print("Hello World!")

name = "Denis"
print(name)

print(11 // 3)
# prints 3 (whole division)

multi_line_string = '''this is
a multiline
string'''

print(multi_line_string)
print("%s" % (multi_line_string))

array = ['a', 'b', 'c', 'd', 'e']
print(array[1:3]) # ['b', 'c'] - excluding 3rd element
array.append('f')
array.insert(0, 'aa')
array.remove('b')
del array[2]
print(array) # ['aa', 'a', 'd', 'e', 'f']

array += ['g', 'h']
print(array) # ['aa', 'a', 'd', 'e', 'f', 'g', 'h']
print(len(array), min(array), max(array)) # (7, 'a', 'h')

pi_tuple = (3, 1, 4, 1, 5, 9, 2, 6)
pi_tuple.append(1) # error - tuples are immutable
pi_tuple[0] = 33 # error - tuples are immutable
