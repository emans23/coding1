try:
    num1,num2=eval(input("enter two number seperated by a comma"))
    result=num1/num2
    print("result is ",result)
except ZeroDivisionError:
    print("divisibleby zero is error")
except SyntaxError:
    print("comma is missing")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")                
         