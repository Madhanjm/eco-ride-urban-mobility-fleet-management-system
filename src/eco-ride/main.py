from vehicle import Vehicle,ElectricCar,ElectricScooter

class EcoRideMain:
    def greet(self):
        print("Welcome to Eco-Ride Urban Mobility System")
        
    def calculate_cost(self):
        es1=ElectricScooter("ES-1","ES1",50,90)
        es2=ElectricScooter("ES-2","ES2",60,85)
        ec1=ElectricCar("EC-1","Ec1",50,4) 
        ec2=ElectricCar("EC-2","Ec2",50,5) 
        list=[es1,es2,ec1,ec2]
        for i in list:
            cost=i.calculate_trip_cost(1)
            print(f"{i.model} trip coast : {cost}")
            
er=EcoRideMain()
er.calculate_cost()

        

        
