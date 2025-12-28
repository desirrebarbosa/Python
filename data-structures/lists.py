# a list is a sequenced collection of different objects

L = ["The Bodyguard", 7.0, 1992, "BG", 1]
print(L)

# the very top of the stack or
# the very last of the string
# starts with negative 1
print("Using negative indexing ", L[-3])

# lists can list tuples and list as well
mylist = ["The Bodyguard", 7.0, [1.1, "inside a list of a list"], ("A", 1)]
print(mylist)

# list slicing
print(L[3:5])

# use .extend to concat or add elements on the list
L.extend(['pop', 10])
# can also use append
L.append(['pop1', 101])
print(L)

# quiz on list
a_list = [1, 'hello', [1, 2, 3], True]
print(a_list[1])
# note that the start is inclusive but the stop is inclusive
print(a_list[1:4])

A = [1, 'a']
B = [2, 1, 'd']
C = A + B
print(C)