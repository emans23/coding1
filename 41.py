def cube(number):
    return number*number*number
def by_three(number):
    if number%3==0:
        print (cube(number))
    else:
        return False
by_three(9)    