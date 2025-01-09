from functools import reduce


l = [2,5,8,10,15,67,65,86,75]

def maxNum(a,b):
    if(a > b):
        return a
    
    return b


li = reduce(maxNum, l)

print(li)

