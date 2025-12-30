import pytest
from eco_ride.vehicle import ElectricCar
@pytest.fixture
def car():
    car= ElectricCar("id","base",85,4)
    return car

def test_car_instance(car):
    assert car.vehicle_id == "id"
    assert car.model =="base"
    assert car.battery_level==85
    assert car.seating_capacity==4
    
def test_car_trip_cost(car):
    car.calculate_trip_cost(5)==5+(0.5*5)
    
def test_car_set_rental_price(car):
    car.rental_price=50
    assert car.rental_price==50

def test_car_rental_exception(car):
    with pytest.raises(ValueError):
        car.rental_price=-50
        assert car.rental_price==None
        
def test_car_set_maintence_status(car):
    car.maintenance_status="Available"
    assert car.maintenance_status=="Available"
    
def test_car_maintenec_status_exception(car):
    with pytest.raises(ValueError):
        car.maintenance_status="dont know"

def test_car_battery(car):
    car.battery_level=80
    assert car.battery_level==80
    
def test_car_battery_exception(car):
    with pytest.raises(ValueError):
        car.battery_level=120