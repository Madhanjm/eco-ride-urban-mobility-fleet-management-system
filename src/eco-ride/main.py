from vehicle import Vehicle

class EcoRideMain:
    def greet(self):
        print("Welcome to Eco-Ride Urban Mobility System")
        
    def basic_fleet_setup(self):
        v1=Vehicle("v1","v1-E",50)
        return v1
    
    def check_security(self):
        v1=Vehicle("v1","v1-E",50)
        print(v1.battery_level)
        print(v1.rental_price)
        v1.rental_price=10
        print(v1.rental_price)
        print(v1.maintenance_status)
        v1.maintenance_status="good"
        print(v1.maintenance_status)
    
        
er=EcoRideMain()
er.check_security()
        
