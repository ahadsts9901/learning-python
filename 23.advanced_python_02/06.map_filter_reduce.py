from functools import reduce


# map

l = [2,3,4,5,6]
square = lambda x : x * x

sqlist = map(square, l)
print(list(sqlist))


# filter

f = [2,3,6,5,9,8]

def even(n):
    if n%2 == 0:
        return True

    return False

even_list = list(filter(even, f))
print(even_list)


# reduce

s = [1,2,3,4,5,6,7]

def sum(a,b):
    return a + b

mul = lambda x, y : x * y

red_sum = reduce(sum, s)
red_mul = reduce(mul, s)

print(red_sum)
print(red_mul)

