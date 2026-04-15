class vehicle:
    def __init__(self,name,maxspeed,milage):
        self.name=name
        self.maxspeed=maxspeed
        self.milage=milage
class bus(vehicle):
    pass
school_bus=bus("school volvo",180,12)
print("bus name:",school_bus.name,"max speed",school_bus.maxspeed,"milage",school_bus.milage)
