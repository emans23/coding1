mc= input("do you have a medical case? (Y/N)").strip().upper()
if mc=="Y":
    print("allowed to take the exam")
else:
    att=int(input("enter your atendance"))    
    if att>75:
        print("you are allowed to take the exam")
    else:
        print("you are not allowed")    
                                            