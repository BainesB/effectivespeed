# This is the second biggest cost of motoring. 
# Might want to track the users milage. 
# Working litres per mile.
# Assuming 0.129888339 litres per mile. based on 35 miles per gallon. 

import sys
sys.path.insert(0, '/home/alex/effectivespeed') 
import constants

LitersPerMile = constants.LitersPerMile 
WorkingDaysPerYear = constants.WorkingDaysPerYear # import this value. 
#FuelPriceLiters = #want to get this from the web. 

def daily_fuel_Cost(miles_per_year, fuel_price_liters, litres_per_mile, working_days_per_year):
    litres = litres_per_mile * miles_per_year
    fuel_cost = litres * fuel_price_liters
    daily_fuel_Cost = fuel_cost / working_days_per_year
    return daily_fuel_Cost
'''
# test code: 
result = daily_fuel_Cost(7000,1.29, LitersPerMile, WorkingDaysPerYear)
print('Daily fuel cost: GDP', result)
'''
