class BMW:
    def start_engine(self):
        return "BMW engine starts with a smooth purr."

    def top_speed(self):
        return "BMW top speed: 250 km/h"

    def display_info(self):
        return "This is a BMW - luxury and performance combined."
class Ferrari:
    def start_engine(self):
        return "Ferrari engine roars with a powerful growl!"

    def top_speed(self):
        return "Ferrari top speed: 340 km/h"

    def display_info(self):
        return "This is a Ferrari - built for speed and racing heritage."
def show_car_details(car):
    print(car.start_engine())
    print(car.top_speed())
    print(car.display_info())
    print("-" * 40)
bmw_car = BMW()
ferrari_car = Ferrari()
print("=== BMW Details ===")
show_car_details(bmw_car)

print("=== Ferrari Details ===")
show_car_details(ferrari_car)
