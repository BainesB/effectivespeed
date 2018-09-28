import nose
from CleanUp import CleanUp_Car_Price, CleanUp_Car_Name, CleanUp_Notes
# want to test my clearup functions. 

#Car Price >> [<span class="actual-price">£4,999</span>]

def test_CleanUp_Car_Price():
    price = CleanUp_Car_Price('<span class="actual-price">£4,999</span>') 
    assert price == 4999
def test_CleanUp_Car_Name():
    name = CleanUp_Car_Name('<h3>Vauxhall Agila</h3>')
    assert name == 'Vauxhall Agila'
   
def test_CleanUp_Reff():
    pass



def test_CleanUp_Notes():
    list = CleanUp_Notes('<p>MPV, Manual, Petrol, Grey, 2011 (11), 53,104 miles</p>')

    assert list[0] == 2011
    assert list[1] == 53104



