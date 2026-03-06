str=input("enter a word")
str.lower()
for i in str:
    if i=="a":
        print("a is found")
        break
    else:
        print("a is not found")