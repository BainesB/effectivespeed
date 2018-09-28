# working out how much time it pay for the petrol. 
import sys
sys.path.insert(0, '/home/alex/effectivespeed')
import constants
from getsalaryinforfromdb import getusersalarybreakdown 
from fuelCost import daily_fuel_Cost

MilesPerYear = constants.MilesPerYear # this should be a constant.ppl may want to change it.  
FuelPrice = constants.FuelPrice 
LitresPerMile = constants.LitersPerMile
WorkingDaysPerYear = constants.WorkingDaysPerYear 
HoursWorkedPerDay = constants.HoursWorkedPerDay
def fuelcostastime(salary):
    Salary = salary
    Daily_Take_Home_Pay = getusersalarybreakdown((salary/1000))
    print('They make', Daily_Take_Home_Pay, 'per day')
    Daily_Fuel_Cost = daily_fuel_Cost(MilesPerYear,FuelPrice,LitresPerMile,WorkingDaysPerYear)
    print('The fuel is costing them', Daily_Fuel_Cost, 'per day')
    calc = (Daily_Fuel_Cost/Daily_Take_Home_Pay) * HoursWorkedPerDay

    HoursWork_per_DailyFuelCost = int(calc)
    Miniutes_per_DailyFuelCost = (calc *60) % 60
    return HoursWork_per_DailyFuelCost, Miniutes_per_DailyFuelCost
# test code
'''
for i in range(30000, 40000, 1000):
    X = fuelcostastime(i)
    print('Hour Per Day worked to pay for fuel:',X[0])
    print('Minutes Per Day worked to pay for fuel:',X[1])
    '''
