# get car gaint https://www.cargiant.co.uk/search/all/all
import sqlite3
import bs4
import requests
from CleanUp import CleanUp_Car_Price, CleanUp_Car_Name, CleanUp_Notes
import time
# i now have the first page of result(cargiant.co.uk/search/all/all) in my db. 
# to get the restest of the website, in need to interate over cargiant.co.uk/search/all/all/page/2) 

for i in range(55,85):
    time.sleep(1)
    pagestr = '/page/' + str(i)
    url = 'https://www.cargiant.co.uk/search/all/all'
    urlstring = url + pagestr
    res = requests.get(urlstring)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    span = soup.find_all('span', {'class' : 'actual-price'})
    vehicles = soup.find_all('li', {'class' : 'vehicle'})

    for i in vehicles:
        Car_Price = CleanUp_Car_Price(str(i.find_all('span', {'class' : 'actual-price'})[0]))
        Car_info_tab = i.find_all('div', {'class' : 'small-7 columns'})
        first_thing = Car_info_tab[0]
        Car_Make = CleanUp_Car_Name(str(first_thing.select('h3')[0])).replace(' ','_')
    
        Ref = str(i.find_all('div', {'class' : 'ref-views'})[0])[36:43]
        Car_Age_Milage = CleanUp_Notes(str(first_thing.select('p')[1]))
        Year = Car_Age_Milage[0]
        Mileage = Car_Age_Milage[1]

        print('Reff:', Ref)
        print('Car Price:', Car_Price)
        print('Car Make:', Car_Make)
        print('Year:',Year)
        print('Mileage:',Mileage) 
        #Car_Age_Milage, is notes. 
    
        ## Put this stuff in a db 

        conn =sqlite3.connect('Cars.db')
        cursor = conn.cursor()
   
        cursor.execute(f'''
        INSERT INTO cars (Ref, car_price, car_make, year, mileage)
        VALUES('{Ref}',{Car_Price},'{Car_Make}',{Year},{Mileage});
        ''' )

        conn.commit()
        cursor.close()
        conn.close()


## can't realy see why it is breaking accept that it might be an artifact something else. 
## Would be good to store the page number you got to when it breaks. 
