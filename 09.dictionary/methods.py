_empty_dictionary = {}

_dictionary = {
    "name": "Ahad",
    "age": 19,
    "languages": ["python", "javascript"]
}

# get keys & values

print(_dictionary.keys())
print(_dictionary.values())
print(_dictionary.items())

# update

_dictionary["name"] = "Abdul Ahad"
print(_dictionary)

_dictionary.update({"age": 19.5})
print(_dictionary)

# type

print(type(_dictionary["languages"]))

# add

_dictionary["city"] = "karachi"
print(_dictionary)

# get

print(_dictionary["age"])
print(_dictionary.get("age"))

# remove

_removed_dict = _dictionary.pop("languages")
print(_removed_dict)

print(_dictionary)

# checking keys

print("age" in _dictionary)

# copying dictionary

copied_dict = _dictionary.copy()
print(copied_dict)

# clearing dictionary

_dictionary.clear()
print(_dictionary)