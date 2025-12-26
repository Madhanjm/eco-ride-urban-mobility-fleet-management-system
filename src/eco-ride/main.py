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
        
        status = input("Enter Vehicle Status (Available / On Trip / Under Maintenance): ").title()
        try:
            vehicle.set_maintenance_status(status)
        except ValueError as e:
            print(e)
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
            
    def search_by_hub_location(self,hub_name):
        if hub_name not in self.fleet_hub:
            print(f"{hub_name} not found")
            return
        
        vehicles=self.fleet_hub[hub_name]
        
        if not vehicles:
            print(f"No Vehicles at {hub_name}")
            return
        
        print(f"Vehicle in {hub_name}")
        for i in vehicles:
            print(f"VEHICLE ID :{i.vehicle_id}|VEHICLE MODEL :{i.model}|VEHICLE BATTERY :{i.battery_level}%")
            
    def catagorized_view(self):
        catagory_vehicle={"car":[],"scooter":[]}
        
        for vehicles in self.fleet_hub.values():
            for v in vehicles:
                if isinstance(v,ElectricCar):
                    catagory_vehicle["car"].append(v)
                elif isinstance(v,ElectricScooter):
                    catagory_vehicle["scooter"].append(v)

        for catagory,vehicles in catagory_vehicle.items():
            print(f"---{catagory}---")
            if not vehicles:
                print("No vehicles in catagory")
                continue
            
            for v in vehicles:
                  print(f"VEHICLE ID :{v.vehicle_id} | VEHICLE MODEL :{v.model} | VEHICLE BATTERY :{v.battery_level}%")
                  
    def fleet_analytics(self):
        status_count={"Available":0,"On Trip":0,"Under Maintenance":0}
        for vehicles in self.fleet_hub.values():
            for v in vehicles:
                if v.status in status_count:
                    status_count[v.status]+=1
        
        print("---Fleet Analytics---")
        print(f"Available Vehicle : {status_count['Available']}")
        print(f"On Trip Vehicle : {status_count['On Trip']}")
        print(f"Under Maintenance Vehicle : {status_count['Under Maintenance']}")
        print("--------------------------------------")
        
    def sort_vehicles_by_model(self,hub_name):
        if hub_name not in self.fleet_hub:
            print(f"Hub {hub_name} not found")
            return

        vehicles = self.fleet_hub[hub_name]

        if not vehicles:
            print(f"No Vehicles at {hub_name}")
            return

        sorted_vehicles = sorted(vehicles, key=lambda v: v.model.lower())

        print(f"Vehicles in {hub_name} sorted by Model")
        for v in sorted_vehicles:
            print(v)
        
    def sort_vehicles_by_battery(self,hub_name):
        if hub_name not in self.fleet_hub:
            print(f"Hub {hub_name} not found")
            return

        vehicles = self.fleet_hub[hub_name]

        if not vehicles:
            print(f"No Vehicles at {hub_name}")
            return

        sorted_vehicles = sorted(vehicles, key=lambda v: v.battery_level,reverse=True)

        print(f"Vehicles in {hub_name} sorted by Battery By High To Low")
        for v in sorted_vehicles:
            print(v)
        
        
if __name__ == "__main__":
    er=EcoRideMain()
    while True:
        print("1.Add New Hub")
        print("2.Add Vehicle to Existing Hub")
        print("3.Search Vehicle by Hub Location(Hub Name)")
        print("4.search by category ")
        print("5.Fleet Analytics")
        print("6.Sort By Vehicle using model")
        print("7.Sort Vehicle By Battery")
        print("8.Exit")
        
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
                hub_name=input("Enter the Hub Location(Hub Name) to search vehicles :")
                er.search_by_hub_location(hub_name)
                
            case 4:
                er.catagorized_view()
                
            case 5:
                er.fleet_analytics()
                
            case 6:
                er.sort_vehicles_by_model(hub_name)
            
            case 7:
                er.sort_vehicles_by_battery(hub_name)
                    
            case 8:
                    print(f"{er.fleet_hub}")
                    print("Exited!!")
                    break
            case _:
                print("Invalid choice")

        

        
