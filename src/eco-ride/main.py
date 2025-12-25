from vehicle import Vehicle,ElectricCar,ElectricScooter

class EcoRideMain:
    def __init__(self):
        self.fleet_hub={}

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
            
    def add_hub(self,hub_name):
        if hub_name in self.fleet_hub:
            print(f"Hub {hub_name} is already present")
        else:
            self.fleet_hub[hub_name]=[]
            print(f"Hub {hub_name} added successfully")   
            
    def add_vehicle(self,hub_name):
        vehicle_type=input("Enter the Vehicle Type(car or scooter):").lower()
        
        if vehicle_type=="car":
            vehicle_id=input("Enter Vehicle ID :")
            vehicle_model=input("Enter Vehicle Model :")
            vehicle_battery=int(input("Enter Vehicle Battery :"))
            vehicle_seats=int(input("Enter Seating Capacity :"))
            vehicle=ElectricCar(vehicle_id,vehicle_model,vehicle_battery,vehicle_seats)
            
            
        elif vehicle_type=="scooter":
            vehicle_id=input("Enter Vehicle ID :")
            vehicle_model=input("Enter Vehicle Model :")
            vehicle_battery=int(input("Enter Vehicle Battery :"))
            vehicle_max_speed=int(input("Enter Vehicle Max Speed :"))
            vehicle=ElectricScooter(vehicle_id,vehicle_model,vehicle_battery,vehicle_max_speed)
            
        else:
            print("Invalid Type")
            return
        
        if self.duplicate_check(hub_name,vehicle):
            return
        self.fleet_hub[hub_name].append(vehicle)
        print(f"{vehicle_id} id added to {hub_name}")
        
    def duplicate_check(self,hub_name,vehicle):
        existing_vehicles=self.fleet_hub[hub_name]
        if any([v==vehicle for v in existing_vehicles]):
            print(f"Duplicate found at {vehicle.vehicle_id} in {hub_name}")
            return True
        return False
            
if __name__ == "__main__":
    er=EcoRideMain()
    while True:
        print("1.Add New Hub")
        print("2.Add Vehicle to Existing Hub")
        print("3.Exit")
        
        choice=int(input("Enter Your choice :"))
        
        match choice:
            case 1:
                hub_name=input("Enter Hub Name :")
                er.add_hub(hub_name)
                        
            case 2:
                hub_name=input("Enter Hub Name to add vehicles :")
                if hub_name not in er.fleet_hub:
                    print(f"Hub {hub_name} not present")
                    continue
                er.add_vehicle(hub_name)
                    
            case 3:
                    print(f"{er.fleet_hub}")
                    print("Exited!!")
                    break
            case _:
                print("Invalid choice")

        

        
