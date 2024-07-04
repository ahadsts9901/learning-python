_list = [1, "str", 90, False, None]
_nums = [1, 4, 2, 7, 44, 90, 23, 76]

print(_list)  # [1, 'str', 90, False, None]

# append "new" to _list
_list.append("new")
print(_list)  # [1, 'str', 90, False, None, 'new']

# remove "str" from _list
_list.remove("str")
print(_list)  # [1, 90, False, None, 'new']

# insert 88 at index 2 in _list
_list.insert(2, 88)
print(_list)  # [1, 90, 88, False, None, 'new']

# pop element at index 3 from _list
popped_value = _list.pop(3)
print(popped_value)  # False
print(_list)  # [1, 90, 88, None, 'new']

# clear _list
_list.clear()
print(_list)  # []

# Trying to find index of 1 in an empty list will raise a ValueError
# print(_list.index(1))  # This line will raise ValueError: 1 is not in list

# reverse _list (this modifies _list in place, so it returns None)
_nums.reverse()
print(_nums)  # ['new', None, 88, 90, 1]

# length of _list
print(len(_list))  # 5

# sort _nums (this modifies _nums in place, so it returns None)
_nums.sort()
print(_nums)  # [1, 2, 4, 7, 23, 44, 76, 90]

# count occurrences of "str" in _list
print(_nums.count(1))  # 0 (since "str" was removed earlier)

# min and max of _list
print(min(_nums))  # None
print(max(_nums))  # 'new'