class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("blu",10)
woo=parrot("woo",15)
print(blu.species)    
print(woo.species)    
