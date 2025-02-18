#Task4 - Functions and Duck Typing
#CS4300 Zachary Donnelly

#calculates a final price for an item after taking price and discount input
def calculate_discount(price,discount):
    #final price and total discount
    fprice = 0
    tdiscount = 0
    
    tdiscount = price * (discount / 100)
    print(tdiscount)
    
    fprice = price - tdiscount
    print(fprice)
    
    return fprice
    
calculate_discount(100,10)
calculate_discount(100.5,10)
calculate_discount(100, 10.5)
calculate_discount(100.5, 10.5)

#testing calculate_discount for multiple data types and values
def test_calculate_discount():
    
    #both ints
    output = calculate_discount(100,10)
    assert output == 90
    
    #float and int
    output = calculate_discount(100.5,10)
    assert output == 90.45
    
    #int and float
    output = calculate_discount(100, 10.5)
    assert output == 89.5
    
    #both floats
    output = calculate_discount(100.5, 10.5)
    assert output == 89.9475