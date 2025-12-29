from abc import ABC,abstractmethod
class Vehicle(ABC):
    """
        Abstract base class representing a generic electric vehicle.
        Enforces fare calculation and encapsulates sensitive data.
        """
    def __init__(self,vehicle_id,model,battery_level):
        """
        Initializes a vehicle with basic details.

        :param vehicle_id: Unique identifier for the vehicle
        :param model: Vehicle model name
        :param battery_level: Current battery percentage (0–100)
        """
        self.vehicle_id=vehicle_id
        self.model=model
        self.battery_level=battery_level
        self.__rental_price=None
        self.__maintenance_status=None
        self.status=None
    
    def __str__(self):
         """
        Returns a  string representation of the vehicle.
        """
         return f"ID:{self.vehicle_id} | Model:{self.model} | Battery:{self.battery_level}% | Status: {self.status}"
     
    def __eq__(self, other):
        """
    Compares two vehicles based on their vehicle ID.

    :param other: Another Vehicle object
    :return: True if vehicle IDs match, else False
        """
        if not isinstance(other,Vehicle):
            return False
        return self.vehicle_id==other.vehicle_id
        
    def get_rental_price(self):
        return self.__rental_price
    
    def set_rental_price(self,price):
        if price<0:
            raise ValueError("Negative rental price not allowed")
        self.__rental_price=price        
    rental_price=property(get_rental_price,set_rental_price)
    
    def get_maintenance_status(self):
        return self.__maintenance_status
    
    def set_maintenance_status(self,status):
        allowed = ["Available", "On Trip", "Under Maintenance"]
    
        if status not in allowed:
                raise ValueError("Invalid status. Allowed: Available, On Trip, Under Maintenance")
            
        self.__maintenance_status = status
        self.status = status 
             
    maintenance_status=property(get_maintenance_status,set_maintenance_status)
    
    def get_battery_level(self):
        return self.__battery_level
    
    def set_battery_level(self,percentage):
        if not  0<=percentage<=100:
            raise ValueError("Battery Level should in Between 0 to 100")
        self.__battery_level=percentage
        
    battery_level = property(get_battery_level, set_battery_level)
    
    @abstractmethod
    def calculate_trip_cost(self,distance):
        pass
    
class ElectricCar(Vehicle):
    def __init__(self,vehicle_id,model,battery_level,seating_capacity):
        super().__init__(vehicle_id,model,battery_level)
        self.seating_capacity=seating_capacity
        
    def calculate_trip_cost(self, distance):
        return 5 + (0.5*distance)   
     
class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_level,max_speed_limit):
        super().__init__(vehicle_id, model, battery_level)
        self.max_speed_limit=max_speed_limit
    
    def calculate_trip_cost(self, distance):
        return 1 + (0.15 * distance)