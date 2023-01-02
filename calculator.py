#adding function
def add(a,b,c):
    return (a+b+c)
#substracting function
def sub(a,b):
    return(a-b)
#multiplying function
def mul(a,b,c):
    return(a*b*c)
#deviding function
def dev(a,b):
    return(a/b)

action = int(input( "Please, choose the action by using the following number:1 Adding,2 Substraction, 3 Multiplication, 4 Devision:"))
a = int(input("First number:"))
b = int(input("Second number:"))


import logging
logging.basicConfig(level=logging.INFO)
if action == 1:
    c = int(input("Third number:"))
    result = add(a,b,c)
    result = "The result is " + str(result)
    logging.info("Adding of " + str(a) + ' and '+ str(b) + ' and ' + str(c))
    print (result)
    if result == int:
        print ("This is integer.")
    else:
        print ("This is string,not integer.")

elif action == 2:
    result = sub(a,b)
    result = "The result is " + str(result)
    logging.info("Substraction of " + str(a) + ' and '+ str(b))
    print (result)
    if result == int:
        print ("This is integer.")
    else:
        print ("This is string,not integer.")

elif action == 3:
    c = int(input("Third number:"))
    result = mul(a,b,c)
    result = "The result is " + str(result)
    logging.info("Multiplication of " + str(a) + ' and '+ str(b) + ' and ' + str (c))
    print (result)
    if result == int:
        print ("This is integer.")
    else:
        print ("This is string, not integer.")

elif action == 4:
    result = dev(a,b)
    result = "The result is " + str(result)
    logging.info("Devision of " + str(a) + ' and '+ str(b))
    print (result)
    if result == int:
        print ("This is integer.")
    else:
        print ("This is string,not integer.")

else:
    print("Invalid input")