# need to clean up the stuff I've pulled off the website. 

def CleanUp_Car_Price(pricestring):
    newstr = pricestring.strip('<span class="actual-price">£')
    newstr2 = newstr.strip('</span>')
    newstr3 = newstr2.replace(',','')

    return int((newstr3))
def CleanUp_Car_Name(namestring):
    newstr = namestring.strip('<h3>')
    newstr2 = newstr.strip('</')
    return newstr2 

def CleanUp_Notes(notestring):
    newstr = notestring.strip('<p>')
    newstr2 = newstr.strip('</')
    
    list = newstr2.split(',')
    year = int(str(list[4])[1:5])
    prefixNum = str(list[5])
    sufixNum = str(list[6].strip(' miles'))
    milestr = prefixNum + sufixNum
    miles = int(milestr)

    print('Year:',year,'Miles',miles)
    return year, miles

X = CleanUp_Notes('<p>MPV, Manual, Petrol, Grey, 2011 (11), 53,104 miles</p>')
