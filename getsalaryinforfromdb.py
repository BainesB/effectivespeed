# this is need to get salary break down stuff from the db.
import sys

import sqlite3

# User enters a salary. 
# get break down form db
# return that break down to a var here so I can use it. 

def getusersalarybreakdown(salaryIn_K):
    UserSalary = salaryIn_K*1000

    conn = sqlite3.connect('scrapy/salaryTable.db')
    cursor = conn.cursor()

    user_salary_breakdown = cursor.execute(f'''
    select GROSE_ANNUAL_SALARY, Daily_Grose_Pay, Daily_Take_Home_Pay from salaryBreakdown where GROSE_ANNUAL_SALARY = {UserSalary}''')
    for i in user_salary_breakdown: 

        returned_user_salary = i[0]
        print('returned_user_salary:', returned_user_salary)
        returned_user_Daily_Grose = i[1]
        print('returned_user_Daily_Grose:', returned_user_Daily_Grose)
        returned_user_Daily_Take_Home = i[2]
        print('returned_user_Daily_Take_Home:', returned_user_Daily_Take_Home)
        return returned_user_Daily_Take_Home
        print('=='*50)
    cursor.close()
    conn.close()
# we need to work out what happens when someone make more money than you have put in the db. 
