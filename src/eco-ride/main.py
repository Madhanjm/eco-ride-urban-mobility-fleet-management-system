from vehicle import Vehicle

class EcoRideMain:
    def greet(self):
        print("Welcome to Eco-Ride Urban Mobility System")
        
    def basic_fleet_setup(self):
        v1=Vehicle("v1","v1-E",50)
        return v1
        
er=EcoRideMain()
print(er.basic_fleet_setup().model)
        
