try:
    age=int(input("enter your age"))
    if age<0:
        print("age cannot be negative")
    else:
        print("valid age entered")
        if age % 2==0:
            print("the age is even")
        else:
            print("the age is odd")     
except ValueError:
    print("invalid input. please enter a whole number ")               
finally:
    print("program finished.")    