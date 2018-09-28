# import the constaint ved per day. 
# import the pay
# return the mins and the hours

import sys
sys.path.insert(0, '/home/alex/effectivespeed')
import constants
from getsalaryinforfromdb import getusersalarybreakdown


VEDperDay = constants.VEDperDay
HoursWorkedPerDay = constants.HoursWorkedPerDay 

def VEDastime(salary):
    Salary = salary
    Daily_Take_Home_Pay = getusersalarybreakdown((salary/1000))
    print('They make', Daily_Take_Home_Pay, 'per day')
    Daily_VED_Cost = VEDperDay
    print('The VED is costing them', Daily_VED_Cost, 'per day')
    calc = (Daily_VED_Cost/Daily_Take_Home_Pay) * HoursWorkedPerDay

    HoursWork_per_DailyVEDCost = int(calc)
    Miniutes_per_DailyVEDCost = (calc *60) % 60
    return HoursWork_per_DailyVEDCost, Miniutes_per_DailyVEDCost

# Test Code
X = VEDastime(32000)
print('VED Hrs:',X[0],'VED mins:',int(X[1]))
