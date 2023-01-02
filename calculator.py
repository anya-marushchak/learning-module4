#adding function
def add(a,b):
    return (a+b)
#substracting function
def sub(a,b):
    return(a-b)
#multiplying function
def mul(a,b):
    return(a*b)
#deviding function
def dev(a,b):
    return(a/b)

action = int(input( "Please, choose the action by using the following number:1 Adding,2 Substraction, 3 Multiplication, 4 Devision:"))
a = int(input("First number:"))
b = int(input("Second number:"))

import logging
logging.basicConfig(level=logging.INFO)
if action == 1:
    result = add(a,b)
    result = "The result is " + str(result)
    logging.info("Adding of " + str(a) + ' and '+ str(b))
    print (result)
elif action == 2:
    result = sub(a,b)
    result = "The result is " + str(result)
    logging.info("Substraction of " + str(a) + ' and '+ str(b))
    print (result)
elif action == 3:
    result = mul(a,b)
    result = "The result is " + str(result)
    logging.info("Multiplication of " + str(a) + ' and '+ str(b))
    print (result)
elif action == 4:
    result = dev(a,b)
    result = "The result is " + str(result)
    logging.info("Devision of " + str(a) + ' and '+ str(b))
    print (result)
else:
    print("Invalid input")