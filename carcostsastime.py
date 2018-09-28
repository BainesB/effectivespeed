import sys
sys.path.insert(0, '/home/alex/effectivespeed/depreciation')
sys.path.insert(0, '/home/alex/effectivespeed/fuelCost')
sys.path.insert(0, '/home/alex/effectivespeed/servicing')
sys.path.insert(0, '/home/alex/effectivespeed/VED')
sys.path.insert(0, '/home/alex/effectivespeed/insurance')
import constants
from depreciationAsTime import depreciationAsTime
from fuelCostAsTime import fuelcostastime
from servicingAsTime import ServicingMaintenanceCostAsTime
from VEDAsTime import VEDastime
from insuranceAsTime import InsuranceCostAsTime

def TotalCarCostTime(salary, CarPurchasePrice, HoldingYears,DepRate):

    DepTime = depreciationAsTime(salary, CarPurchasePrice, HoldingYears, DepRate) 
    FuelTime = fuelcostastime(salary)
    ServicingTime = ServicingMaintenanceCostAsTime(salary)
    VEDTime = VEDastime(salary)
    InsuranceTime = InsuranceCostAsTime(salary)

    TotalHours = 0
    TotalMins = 0

    listA = [
        DepTime,
        FuelTime,
        ServicingTime,
        VEDTime,
        InsuranceTime
        ]

    for i in listA:
        TotalHours+=i[0]
        TotalMins+=i[1]

    return TotalHours, TotalMins
# Would like to do a for loop here put there is too much stuff printing out. 

X = TotalCarCostTime(38000, 2500, 5,'L')

print('Each day it takes you:')
print(X[0],'hrs', X[1],'mins to pay for your car')

# Bug is if mins go over 60 it needs to add an hour. 





























'''
print('Each day it takes you:')
print(DepTime[0],'hrs', int(DepTime[1]),'mins to pay for the depreseation on your car')
print('Each day it takes you:')
print(FuelTime[0],'hrs', int(FuelTime[1]),'mins to pay for the Fuel your car uses')
print('Each day it takes you:')
print(ServicingTime[0],'hrs', int(ServicingTime[1]),'mins to pay for the Servicing your car uses')
print('Each day it takes you:')
print(VEDTime[0],'hrs', int(VEDTime[1]),'mins to pay for the VED your car uses')

print('Each day it takes you:')
print(InsuranceTime[0],'hrs', int(InsuranceTime[1]),'mins to pay for the Insurance your car uses')

salary = input('enter salary:')
CarPurchasePrice = input('enter the amount you paid for the car')
HoldingYears = input('How long will you have kept the car when you sell it')
DepRate = input('L,A,H')
'''
