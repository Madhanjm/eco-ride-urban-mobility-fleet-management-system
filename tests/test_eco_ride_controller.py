import pytest
from eco_ride.eco_ride_controller import EcoRideMain
from eco_ride.vehicle import *

@pytest.fixture    
def hubS():
    return EcoRideMain()

def test_greet(capsys,hubS):
    hubS.greet()
    captured=capsys.readouterr()
    assert captured.out == "Welcome to Eco-Ride Urban Mobility System\n"
    
def test_calculate_cost(capsys,hubS):
    hubS.calculate_cost()
    captured=capsys.readouterr()
    output=captured.out
    
    assert "ES1 trip coast : 1.15" in output
    assert "ES2 trip coast : 1.15" in output
    assert "Ec1 trip coast : 5.5" in output
    assert "Ec2 trip coast : 5.5" in output
 
def test_add_hubs(hubS):
    hubS.add_hub("Madhan")
    assert "Madhan" in hubS.fleet_hub
    assert hubS.fleet_hub["Madhan"]==[]
    
def test_duplicate_check_by_vehicle_id(hubS):
    hubS.add_hub("Madhan")
    V=ElectricCar("M-1","base",85,4)
    hubS.fleet_hub["Madhan"].append(V)
    
    v1=ElectricCar("M-1","base",85,4)
    
    assert hubS.duplicate_check("Madhan",v1) == True
    
def test_search_by_hub_location(hubS,capsys):
    hubS.add_hub("Madhan")
    V=ElectricCar("M-1","base",85,4)
    hubS.fleet_hub["Madhan"].append(V)
    
    hubS.search_by_hub_location("Madhan")
    captured=capsys.readouterr()
    output=captured.out
    assert "Vehicle in Madhan" in output
    assert "VEHICLE ID :M-1" in output
    assert "VEHICLE MODEL :base" in output
    assert "VEHICLE BATTERY :85%" in output
    
def test_catagorized_view(hubS,capsys):
    hubS.add_hub("Madhan")
    car=ElectricCar("E-1","base",85,4)
    scooter=ElectricScooter("S-1","pro",85,80)
    
    hubS.fleet_hub["Madhan"].extend([car,scooter])
    hubS.catagorized_view()
    
    captured=capsys.readouterr()
    output=captured.out
    
    assert "---car---" in output
    assert "VEHICLE ID :E-1" in output
    assert "VEHICLE MODEL :base" in output
    assert "VEHICLE BATTERY :85%" in output
    
    assert "---scooter---" in output
    assert "VEHICLE ID :S-1" in output
    assert "VEHICLE MODEL :pro" in output
    assert "VEHICLE BATTERY :85%" in output
    
    
def test_fleet_analytics_by_status(hubS,capsys):
    hubS.add_hub("Madhan")
    car=ElectricCar("EC-1","base",85,4)
    car.set_maintenance_status("Available")
    
    scooter=ElectricScooter("ES-1","pro",80,80)
    scooter.set_maintenance_status("On Trip")
    
    hubS.fleet_hub["Madhan"].extend([car,scooter])
    result=hubS.fleet_analytics()
    
    captured=capsys.readouterr()
    output=captured.out
    
    assert "Available Vehicle : 1" in output
    assert "On Trip Vehicle : 1" in output
    assert "Under Maintenance Vehicle : 0" in output
    
    
    
    
    
    
    
