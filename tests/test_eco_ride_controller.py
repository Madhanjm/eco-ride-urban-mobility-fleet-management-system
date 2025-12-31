import os
import pytest
from eco_rides.eco_ride_controller import EcoRideMain
from eco_rides.vehicle import *

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

def test_add_vehicle_car(hubS,monkeypatch,capsys):
    hubS.add_hub("Airport")
    inputs=iter(["car","EC-1","BMW","85","4","Available"])
    monkeypatch.setattr("builtins.input",lambda _:next(inputs))
    hubS.add_vehicle("Airport")
    
    captured=capsys.readouterr()
    output=captured.out
    
    assert "EC-1 id added to Airport" in output
    assert len(hubS.fleet_hub["Airport"])==1
    
def test_add_vehicle_scooter(hubS,monkeypatch,capsys):
    hubS.add_hub("Airport")
    inputs=iter(["scooter","ES-1","pro","85","90","On Trip"])
    monkeypatch.setattr("builtins.input",lambda _:next(inputs))
    hubS.add_vehicle("Airport")
    
    captured=capsys.readouterr()
    output=captured.out
    
    assert "ES-1 id added to Airport" in output
    assert len(hubS.fleet_hub["Airport"])==1
        
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
    
    assert "VEHICLE ID :E-1" in output
    assert "VEHICLE MODEL :base" in output
    assert "VEHICLE BATTERY :85%" in output
    
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
    
def test_sort_vehicle_by_model(hubS,capsys):
    hubS.add_hub("Airpot")
    car=ElectricCar("EC-1","BMW",85,4)
    car1=ElectricCar("Ec-2","AUDI",80,4)
    scooter1=ElectricScooter("ES-1","PRO",75,60)
    
    hubS.fleet_hub["Airpot"].extend([car,car1,scooter1])
    result=hubS.sort_vehicles_by_model("Airpot")
    
    captured=capsys.readouterr()
    output=captured.out
    
    assert "Model:AUDI" in output
    assert "Model:BMW" in output
    assert "Model:PRO" in output
    
    assert output.index("Model:AUDI") < output.index("Model:BMW")
    assert output.index("Model:BMW") < output.index("Model:PRO")
    
def test_sort_by_battery(hubS,capsys):
    hubS.add_hub("Airpot")
    car=ElectricCar("EC-1","BMW",85,4)
    car1=ElectricCar("Ec-2","AUDI",80,4)
    scooter1=ElectricScooter("ES-1","PRO",75,60)
    
    hubS.fleet_hub["Airpot"].extend([car,car1,scooter1])
    result=hubS.sort_vehicles_by_battery("Airpot")
    
    captured=capsys.readouterr()
    output=captured.out
    
    assert "Battery:85" in output
    assert "Battery:80" in output
    assert "Battery:75" in output
    
    assert output.index("Battery:85") < output.index("Battery:80")
    assert output.index("Battery:80") < output.index("Battery:75")
    
def test_save_fleet_to_csv(hubS,tmp_path):
    file_name=tmp_path/"vehicles.csv"
    hubS.save_fleet_to_csv(file_name)
    
    assert file_name.exists()
    
def test_load_fleet_from_csv(hubS,tmp_path):
    car=ElectricCar("EC-1","BMW",85,4)
    car.set_maintenance_status("Available")
    
    scooter=ElectricScooter("ES-1","PRO",75,60)
    scooter.set_maintenance_status("On Trip")
    
    hubS.fleet_hub={"Davangere":[car,scooter]}
    
    file_name=tmp_path/"fleet.csv"
    
    hubS.save_fleet_to_csv(file_name)
    hubS.load_fleet_from_csv(file_name)
    
    
    assert "Davangere" in hubS.fleet_hub
    vehicle = hubS.fleet_hub["Davangere"]
    assert vehicle[0].vehicle_id=="EC-1"
    assert vehicle[1].vehicle_id=="ES-1"

def test_save_fleet_to_json(hubS,tmp_path):
    file_name=tmp_path/"vehicles.csv"
    hubS.save_fleet_to_json(file_name)
    
    assert file_name.exists()
    
def test_load_fleet_from_json(hubS):
    hubS.load_fleet_from_json("src/eco_rides/fleet_data.json")
    
    assert "Airport" in hubS.fleet_hub
    vehicle=hubS.fleet_hub["Airport"]
    
    assert vehicle[0].vehicle_id=="Ec-1"
    assert vehicle[0].model == "base"
    assert vehicle[1].vehicle_id=="ES-2"
    assert vehicle[1].model=="Top"
    
    
    
    
    
    
    
    
    
