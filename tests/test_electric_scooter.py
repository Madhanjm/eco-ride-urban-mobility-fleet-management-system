import pytest
from eco_rides.vehicle import ElectricScooter

@pytest.fixture
def scooter():
    scooter=ElectricScooter("ES-1","pro",85,80)
    return scooter

def test_scooter_instance(scooter):
    assert scooter.vehicle_id == "ES-1"
    assert scooter.model =="pro"
    assert scooter.battery_level==85
    assert scooter.max_speed_limit==80
    
def test_scooter_trip_cost(scooter):
    scooter.calculate_trip_cost(5)==1+(0.15*5)
    
def test_scooter_set_rental_price(scooter):
    scooter.rental_price=20
    assert scooter.rental_price==20
    
def test_scooter_rental_exception(scooter):
    with pytest.raises(ValueError):
        scooter.rental_price=-50
        
def test_scooter_set_maintence_status(scooter):
    scooter.maintenance_status="Available"
    assert scooter.maintenance_status=="Available"
    
def test_scooter_maintence_status_exception(scooter):
    with pytest.raises(ValueError): 
        scooter.maintenance_status="dont know"

def test_scooter_battery(scooter):
    scooter.battery_level=80
    assert scooter.battery_level==80
    
def test_scooter_battery_exception(scooter):
    with pytest.raises(ValueError):
        scooter.battery_level=120
