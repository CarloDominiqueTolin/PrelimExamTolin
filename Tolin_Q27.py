#Carlo Dominique T. Tolin
#CPE41S6

def check_obese(x): return x
def convert_kelvin_to_fahrenheit(y): return y
def area_of_rectangle(a,b): return a*b

def test_if_obese():
    '''Checks if Obese'''
    x = 90 
    y = check_obese(x)
    assert(y>=80)

def test_kelvin_to_fahrenheit():
    '''Converts kelvin to fahrenheit'''
    pass

def test_area_of_rectangle():
    '''returns area of rectangle'''
    a,b = 5, 10
    x = area_of_rectangle(a,b)
    assert(x==(a*b))