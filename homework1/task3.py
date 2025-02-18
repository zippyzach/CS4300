#Task3 - Control Structures
#CS4300 Zachary Donnelly

#if statement to see if a value is positive, negative, or zero
def check_num(x):
    if(x > 0):
        z = "positive"
    elif(x == 0):
        z = "zero"
    else:
        z = "negative"   

    return z

#calculating the first 10 prime numbers and outputs to screen
def primes():
    x = 0
    y = 2
    primes = ""
    
    #while loop for first 10 primes
    while(x < 10):
        prime = True
        
        #for loop to check if prime is false
        for i in range(2, y):
            if y % i == 0:
                prime = False
        
        #if prime is true, store in primes string and increment
        if(prime == True):
            x += 1
            primes += str(y) + " "
  
        #check next number    
        y += 1
    return primes
    
    
#using a while loop to calculate the sum of all values between 1 and 100
def sum():
    x = 0
    output = 0
    
    while(x <= 100):
        output += x
        x += 1
        
    return output
    
    
    


#testing check_num for zero, positive, or negative
def test_check_num():
    output = check_num(0)
    assert output == "zero"
    
    output = check_num(1)
    assert output == "positive"
    
    output = check_num(-1)
    assert output == "negative"
    
#testing primes that the correct first 10 primes were output to the screen    
def test_primes():
    output = primes()
    
    assert output == "2 3 5 7 11 13 17 19 23 29 "
    
    
    
#verifying test_sum calculated the correct value
def test_sum():
    output = sum()
    
    assert output == 5050
    