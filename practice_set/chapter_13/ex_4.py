l = [2,5,8,10,15,67,65,86,75]

def divisible_of_five(n):
    if(n%5 == 0):
        return True
    
    return False


lis = filter(divisible_of_five, l)

print(list(lis))

