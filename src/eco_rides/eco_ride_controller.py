import csv
import json
from .vehicle import Vehicle,ElectricCar,ElectricScooter

class EcoRideMain:
    """
    Main controller class for Eco-Ride Urban Mobility System.
    Manages hubs, vehicles, analytics, sorting, and file persistence.
    """
    def __init__(self):
        self.fleet_hub={}

    def greet(self):
        print("Welcome to Eco-Ride Urban Mobility System")
        
    def menu_interface(self):
        self.load_fleet_from_csv()
        self.load_fleet_from_json()
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
                    self.add_hub(hub_name)
                            
                case 2:
                    hub_name=input("Enter Hub Name to add vehicles :")
                    if hub_name not in self.fleet_hub:
                        print(f"Hub {hub_name} not present")
                        continue
                    self.add_vehicle(hub_name)
                    
                case 3:
                    hub_name=input("Enter the Hub Location(Hub Name) to search vehicles :")
                    self.search_by_hub_location(hub_name)
                    
                case 4:
                    self.catagorized_view()
                    
                case 5:
                    self.fleet_analytics()
                    
                case 6:
                    hub_name=input("Enter the Hub Name")
                    self.sort_vehicles_by_model(hub_name)
                
                case 7:
                    hub_name=input("Enter the Hub Name")
                    self.sort_vehicles_by_battery(hub_name)
                        
                case 8:
                    print(f"{self.fleet_hub}")
                    self.save_fleet_to_csv()
                    self.save_fleet_to_json()
                    print("Exited!!")
                    
                    break
                case _:
                    print("Invalid choice")
  
    def calculate_cost(self):
        """
        Demonstrates polymorphism by calculating trip costs
        for different vehicle types using a common interface.
        """
        es1=ElectricScooter("ES-1","ES1",50,90)
        es2=ElectricScooter("ES-2","ES2",60,85)
        ec1=ElectricCar("EC-1","Ec1",50,4) 
        ec2=ElectricCar("EC-2","Ec2",50,5) 
        list=[es1,es2,ec1,ec2]
        for i in list:
            cost=i.calculate_trip_cost(1)
            print(f"{i.model} trip coast : {cost}")
            
    def add_hub(self,hub_name):
         """
          Adds a new fleet hub to the system.
         :param hub_name: Name of the hub (string)
         """
         if hub_name in self.fleet_hub:
            print(f"Hub {hub_name} is already present")
         else:
            self.fleet_hub[hub_name]=[]
            print(f"Hub {hub_name} added successfully")   
            
    def add_vehicle(self,hub_name):
        """
        Adds a new ElectricCar or ElectricScooter to an existing hub.
        Performs duplicate ID check and status validation.

        :param hub_name: Name of the hub where vehicle is added
        """
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
         """
        Checks for duplicate vehicle IDs within a hub.

        :param hub_name: Hub name
        :param vehicle: Vehicle object
        :return: True if duplicate exists, else False
        """
         existing_vehicles=self.fleet_hub[hub_name]
         if any([v==vehicle for v in existing_vehicles]):
            print(f"Duplicate found at {vehicle.vehicle_id} in {hub_name}")
            return True
         return False
            
    def search_by_hub_location(self,hub_name):
        """
        Searches and displays all vehicles available in a given hub.

        :param hub_name: Name of the hub to search
        """
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
        """
        Displays vehicles grouped by their category:
        Electric Cars and Electric Scooters.
        """
        
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
        """
        Displays count of vehicles grouped by status:
        Available, On Trip, Under Maintenance.
         """   
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
        """
        Sorts and displays vehicles in a hub alphabetically by model name.

        :param hub_name: Name of the hub
        """
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
        """
        Sorts and displays vehicles in a hub by battery level
        in descending order.

        :param hub_name: Name of the hub
        """
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
            
    def save_fleet_to_csv(self, filename="fleet_data.csv"):
        """
        Saves the entire fleet hub and vehicle data into a CSV file.

        :param filename: CSV file name
        """
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
    
            writer.writerow(["hub_name", "vehicle_type", "vehicle_id", "model", "battery_level", "status", "extra"])
            
            for hub_name, vehicles in self.fleet_hub.items():
                for v in vehicles:
                    if isinstance(v, ElectricCar):
                        vehicle_type = "car"
                        extra = v.seating_capacity
                    elif isinstance(v, ElectricScooter):
                        vehicle_type = "scooter"
                        extra = v.max_speed_limit
                    else:
                        continue
                    writer.writerow([hub_name, vehicle_type, v.vehicle_id, v.model, v.battery_level, v.status, extra])
        print("Fleet data saved to CSV successfully.")
        
    def load_fleet_from_csv(self, filename="fleet_data.csv"):
        """
        Loads fleet hub and vehicle data from a JSON file.

        :param filename: JSON file name
        """
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    hub_name = row["hub_name"]
                    vehicle_type = row["vehicle_type"]
                    vehicle_id = row["vehicle_id"]
                    model = row["model"]
                    battery_level = int(row["battery_level"])
                    status = row["status"]
                    extra = int(row["extra"])
                    
                    if hub_name not in self.fleet_hub:
                        self.fleet_hub[hub_name] = []
                    
                    # Recreate vehicle
                    if vehicle_type == "car":
                        vehicle = ElectricCar(vehicle_id, model, battery_level, extra)
                    elif vehicle_type == "scooter":
                        vehicle = ElectricScooter(vehicle_id, model, battery_level, extra)
                    else:
                        continue
                    
                    # Set vehicle status
                    vehicle.set_maintenance_status(status)
                    
                    self.fleet_hub[hub_name].append(vehicle)
            print("Fleet data loaded from CSV successfully.")
        except FileNotFoundError:
            print("CSV file not found. Starting with empty fleet.")
            
    def save_fleet_to_json(self, filename="fleet_data.json"):
        """
        Saves the entire fleet hub and vehicle data into a JSON file.

        :param filename: JSON file name
        """    
        data = {}

        for hub_name, vehicles in self.fleet_hub.items():
            data[hub_name] = []

            for v in vehicles:
                if isinstance(v, ElectricCar):
                    vehicle_type = "car"
                    extra = v.seating_capacity
                elif isinstance(v, ElectricScooter):
                    vehicle_type = "scooter"
                    extra = v.max_speed_limit
                else:
                    continue

                data[hub_name].append({
                    "vehicle_type": vehicle_type,
                    "vehicle_id": v.vehicle_id,
                    "model": v.model,
                    "battery_level": v.battery_level,
                    "status": v.status,
                    "extra": extra
                })

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Fleet data saved to JSON successfully.")
        
    def load_fleet_from_json(self, filename="fleet_data.json"):
        """
        Loads fleet hub and vehicle data from a JSON file
        and reconstructs vehicle objects.

        :param filename: JSON file name
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            self.fleet_hub = {}

            for hub_name, vehicles in data.items():
                self.fleet_hub[hub_name] = []

                for v in vehicles:
                    if v["vehicle_type"] == "car":
                        vehicle = ElectricCar(v["vehicle_id"],v["model"],v["battery_level"],v["extra"])
                    elif v["vehicle_type"] == "scooter":
                        vehicle = ElectricScooter(v["vehicle_id"],v["model"],v["battery_level"],v["extra"])
                    else:
                        continue

                    vehicle.set_maintenance_status(v["status"])
                    self.fleet_hub[hub_name].append(vehicle)

            print("Fleet data loaded from JSON successfully.")

        except FileNotFoundError:
            print("JSON file not found. Starting with empty fleet.")
     

    

