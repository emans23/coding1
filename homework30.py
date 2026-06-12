class Vehicle:
    def __init__(self, brand, model, capacity):
        self.brand = brand
        self.model = model
        self.capacity = capacity  
class Bus(Vehicle):
    def __init__(self, brand, model, capacity, fare_per_person):
        super().__init__(brand, model, capacity)
        self.fare_per_person = fare_per_person
    def calculate_total_fare(self, num_passengers):
        if num_passengers < 0:
            return "Invalid number of passengers"
        elif num_passengers > self.capacity:
            return f"Maximum capacity is {self.capacity}, cannot take {num_passengers} passengers"
        else:
            total = num_passengers * self.fare_per_person
            return total
if __name__ == "__main__":
    my_bus = Bus("Mercedes", "Tourismo", 50, 15)
    result1 = my_bus.calculate_total_fare(30)
    print("Total fare:", result1)  
    result2 = my_bus.calculate_total_fare(55)
    print(result2)  
    result3 = my_bus.calculate_total_fare(-2)
    print(result3) 
