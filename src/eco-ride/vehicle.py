class Vehicle():
    def __init__(self,vehicle_id,model,battery_level):
        self.vehicle_id=vehicle_id
        self.model=model
        self.battery_level=battery_level
        self.__rental_price=None
        self.__maintenance_status=None
        
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
         self.__maintenance_status=status      
    maintenance_status=property(get_maintenance_status,set_maintenance_status)
    
    def get_battery_level(self):
        return self.__battery_level
    
    def set_battery_level(self,percentage):
        if not  0<=percentage<=100:
            raise ValueError("Battery Level should in Between 0 to 100")
        self.__battery_level=percentage
        
    battery_level = property(get_battery_level, set_battery_level)
    
class ElectricCar(Vehicle):
    def __init__(self,vehicle_id,model,battery_level,seating_capacity):
        super().__init__(vehicle_id,model,battery_level)
        self.seating_capacity=seating_capacity
     
class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_level,max_speed_limit):
        super().__init__(vehicle_id, model, battery_level)
        self.max_speed_limit=max_speed_limit
    