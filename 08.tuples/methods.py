_tuple = (1, "str", 90, False, None)
_nums = (1, 4, 2, 7, 44, 90, 23, 76)

# Printing the tuple
print(_tuple)  # Output: (1, 'str', 90, False, None)

# splitting the tuple
_splitted_tuple = _tuple[0:3]
print(_splitted_tuple) # Output : (1, "str", 90)

# Counting occurrences of a value in the tuple
print(_tuple.count(False))  # Output: 1 (count of False)

# Finding the index of an element in the tuple
print(_tuple.index(90))  # Output: 2 (index of 90 in the tuple)