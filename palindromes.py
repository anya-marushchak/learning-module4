def checked_palindrome(x):
    """
       Checks wether string is palindrome or not
    """  
    x == x[::-1]
    if (x == x[::-1]):
        return True
    return False
x = str(input())
y = checked_palindrome (x)
 
if (y):
    print("Yes")
else:
    print("No")  

