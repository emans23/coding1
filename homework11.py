num= int(input("enter a decimal number"))
if num == 0:
    print("binary is 0")
else:
    binary= ""   
    n=num
    while n > 0:
        remainder=n%2
        binary=str(remainder)+ binary
        n //=2
    print("Binary is",binary)    