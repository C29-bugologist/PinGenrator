import random #imported the random function 
num = int(input("  Enter '4' to Generate a 4 digit passcode \n  Enter '6' to Generate a 4 digit passcode \n "))
my_range = range(0,9) #Created a range for random sample function
if num == 6:
    print("Your 6 digit code is ")
    print(random.sample(my_range,num))
elif num == 4:  
    print("Your 4 digit code is ")
    print(random.sample(my_range,num))
else:
    print("ERROR**plese enter either 6 or 4**")
    #Used if else statement so a user can only generate 6 digits or 4 digit code and we can give an error message