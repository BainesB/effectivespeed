# I want to pull some basic information of the Cars.db. 

# I'd like to have a look at the distrobution of cars that are being sold in the UK (assuming for now that car giant are some what representitive of the secondary car market in the uk).

import sqlite3
import pygal

conn =sqlite3.connect('Cars.db')
cursor = conn.cursor()



for i in range(1000, 53000, 1000):
    t = i + 1000
    ii= i
    x = cursor.execute(f'''
    select count(*) from cars WHERE car_price BETWEEN {i} and {t};
    ''' )

    for i in x:
        #print(f'''Result Number of cars between £{ii} & £{t} is:''', i[0])
        chart.add(f'''£{ii}-£{t}''',i[0])

conn.commit()
cursor.close()
conn.close()

chart.render_to_png('Cars.png')
