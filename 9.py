amount=int(input("enter your amount"))
note1=amount//500
note2=(amount%500)//100
note3=((amount%500)%100)//50
note4=(((amount%500)%100)%50)//10
print("the number of 500 pound note are",note1)
print("the number of 100 pound note are",note2)
print("the number of 50 pound note are",note3)
print("the number of 10 pound note are",note4)