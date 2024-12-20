a_tuple = 4, 5
print(type(a_tuple))

b_tuple = (5, 6, 7)
print(type(b_tuple))

c_tuple = tuple(["1", "2", "3"])
print(type(c_tuple))

d_tuple = (1, 2, 3, 4, 5)
print(id(d_tuple))

d_tuple += (6, 7)
print(id(d_tuple))


# Create an empty tuple
empty = tuple()
also_empty = ()

# Single tuple
single = (2,)
print(type(single))
