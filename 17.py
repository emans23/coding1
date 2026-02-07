height=float(input("enter your height"))
weight=float(input("enter your weight"))
bmi=weight/(height/100)**2
print("your bmi is",bmi)

if bmi<=18.4:
    print("your under weight")
elif bmi<=24.4:
    print("your healthy")
elif bmi<=30.4:
    print("over weight")
elif bmi<=34.9:
    print("severly over weight") 
else:
    print("obese")               