import sys
sys.path.insert(0, '/home/alex/effectivespeed')
import constants
from getsalaryinforfromdb import getusersalarybreakdown

HoursWorkedPerDay = constants.HoursWorkedPerDay

def InsuranceCostAsTime(salary):
    InsurancePerDay = constants.InsurancePerDay #dayly cost
    Daily_Take_Home_Pay = getusersalarybreakdown((salary/1000))
    calc = (InsurancePerDay/Daily_Take_Home_Pay) * HoursWorkedPerDay

    HoursWork_per_Daily_InsuranceCost = int(calc)
    Miniutes_per_InusranceCostAsTime = (calc *60) % 60
    return HoursWork_per_Daily_InsuranceCost, int(Miniutes_per_InusranceCostAsTime)

# some test code
X = InsuranceCostAsTime(32000)
print('Insuranc will cost you')
print('Hrs', X[0])
print('Min:',X[1])
