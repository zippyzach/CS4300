#Task2 - Variables and Data Types
#CS4300 Zachary Donnelly

#integer example - addition
def integer_ex():
    x = 10
    y = 5
    
    z = x + y
    
    return z
   
#floating point example - division   
def floating_ex():
    x = 4.5
    y = 1.5
    
    z = x / y

    return z
    
#string example - merging two strings    
def string_ex():
    x = "hello "
    y = "world!"
    
    z = x + y
    
    return z
    
    
#boolean example - True or False
def bool_ex():
    z = True
    
    return z
    
    



#testing integer for set values, also verifies that the output is an integer
def test_integer():
    output = integer_ex()
    
    assert isinstance(output, int)
    assert output == 15

#testing floating for set values, also verifies that the output is a float
def test_floating():
    output = floating_ex()
        
    assert isinstance(output, float)
    assert output == 3

#testing string for set values, also verifies that the output is a string
def test_string():
    output = string_ex()
    
    assert isinstance(output, str)
    assert output == "hello world!"


#testing bool for set value, also verifies that the output is a boolean value
def test_bool():
    output = bool_ex()
    
    assert isinstance(output, bool)
    
    assert output == True
    