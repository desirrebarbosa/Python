# string, int, and float can all be stored in a tuple
tuple1 = ("disco", 10, 1.2)
print(tuple1)
# the type is a tuple
print(type(tuple1))

# sorting, tuples are immutable
ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
ratings_sorted = sorted(ratings)
print(ratings)
print(ratings_sorted)

# a tuple can contain a tuple
nested_tuple = (1, 2, ('first', 2), "rock")
print(nested_tuple)
# access nested tuple as you would
# access matrix
print("this is the first element of the nested tuple: ", nested_tuple[2][0])

# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
tuple_length = len(genres_tuple)
print(tuple_length)
print(genres_tuple[3])
print(genres_tuple[3:6])
print(genres_tuple[0:2])
# wrong
print(genres_tuple[tuple_length - 1][2])
# correct
print("disco".find('s'))
C_tuple = (-5, 1, -3)
C_tuple_sorted = sorted(C_tuple)
print(C_tuple_sorted)