_empty_set = set()

_set = {1,2,5,"hi",True}
_set_1 = {1,2,3,4,5}
_set_2 = {5,6,8,2,6}

print(_set)
print(_empty_set)
print(type(_empty_set))
print(type(_set))

# add

_set.add(10)
print(_set)

# update

_set.update({34,35,36})
print(_set)

# remove

_set.remove("hi")
print(_set)

_set.discard("hi") # if not present no error thrown
print(_set)

# funs

_set.pop()
print(_set)

_new_set = _set.copy()
print(_new_set)

_set.clear()
print(_set)


# union & intersection

print(_set_1.union(_set_2))
print(_set_1.intersection(_set_2))

# operators

print(_set_1 - _set_2)
print(_set_2 - _set_1)