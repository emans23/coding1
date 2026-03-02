def add(n,q):
    return n+q
def subtract(n,q):
    return n+q
def multiply(n,q):
    return n*q
def divide(n,q):
    return n/q
print("enter your choice")
print("a add")
print("s subtract")
print("m multiply")
print("d divide")
num_1=int(input("enter number of your choice"))
num_2=int(input("enter number of your choice"))
choice =input("enter what operation you want to perform a/s/m/d") 
if choice=="a":
    print(add(num_1,num_2))
elif choice=="s":
    print(subtract(num_1,num_2))
elif choice=="m":
    print(multiply(num_1,num_2))
elif choice=="d":
    print(divide(num_1,num_2))               