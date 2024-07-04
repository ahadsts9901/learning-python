_str = "HelLoO WOrLd"
_nums = "1234567890"
_new_str = "  i am   human   "
_list = ["1","4","6","9"]
_country = "Pakistan"

print(_str)
print(_str.capitalize())
print(_str.title())
print(_str.upper())
print(_str.lower())
print(_str[0],_str[3])
print(_str[1:6])
print(_nums[0:9:2])
print(_str.find("l"))
print(_str.find("p"))
print(_str.replace("WOrLd", "Mani"))
print(_new_str.strip())
print(_nums.split("4"))
print(_str.join(_list))
print(_country.startswith("Pak"))
print(_country.endswith("ia"))