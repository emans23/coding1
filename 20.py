phisics=int(input("enter your score in phisics"))
maths=int(input("enter your score in maths"))
english=int(input("enter your score in english"))
pe=int(input("enter your score in pe"))
chemistry=int(input("enter your score in chemistry"))
avg= (phisics+maths+english+pe+chemistry)/5
if avg>91:
    print("your mark is very good")
elif avg>80:
    print("you got a good mark")
elif avg>55:
    print("your mark is average")
elif avg>50:
    print("your failed")            