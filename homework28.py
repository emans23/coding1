
class Dog:
    species = "Canis lupus familiaris"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {self.species}")
        print("------------------------")
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")
dog1.display_details()
dog2.display_details()