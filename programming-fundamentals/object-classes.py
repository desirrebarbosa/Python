class Vehicles:
    color = "white"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def assigning_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    def display_properties(self):
        print("Properties of the Vehicle: ")
        print("Color: ", self.color)
        print("Maximum Speed: ", self.max_speed)
        print("Mileage: ", self.mileage)
        print("Seating Capacity: ", self.seating_capacity)

vehicle1 = Vehicles(200, 20)
vehicle1.assigning_seating_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicles(180, 25)
vehicle2.assigning_seating_capacity(4)
vehicle2.display_properties()