def match_word(words):
    crt=0
    list=[]
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            crt=crt+1
            list.append(i)
    print("the list of words with first and last charracter",list)
    return crt
count=match_word(["abc","aba","das","mum","cat"])
print("the number of words that have the same first letter and last letter are",count)