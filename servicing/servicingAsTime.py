# all you need to do is get the dayly take home. 
# divid it buy the constant for servicing. 
# for now, all i'm going to do is assume everyone is at the average. 
# I might be ablte to tweek this when i've scaped car giant. 

import sys
sys.path.insert(0, '/home/alex/effectivespeed')
import constants
from getsalaryinforfromdb import getusersalarybreakdown 

HoursWorkedPerDay = constants.HoursWorkedPerDay

def ServicingMaintenanceCostAsTime(salary):
    ServicingMaintenance = constants.ServicingMaintenance #day numb
    Daily_Take_Home_Pay = getusersalarybreakdown((salary/1000))
    calc = (ServicingMaintenance/Daily_Take_Home_Pay) * HoursWorkedPerDay

    HoursWork_per_Daily_ServicingMaintenanceCost = int(calc)
    Miniutes_per_ServicingMaintenanceCostAsTime = (calc *60) % 60
    return HoursWork_per_Daily_ServicingMaintenanceCost, int(Miniutes_per_ServicingMaintenanceCostAsTime)

# think this is built. Work out how to test it.

X = ServicingMaintenanceCostAsTime(32000)
print(
        'How much time you spend working to pay for car services each day',X[0],'hrs',X[1],'min'
        
    )

## getting that DB error again. 
