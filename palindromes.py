def checked_palindrome(x):
    """
       Checks whether string is palindrome or not
    """  
    x == x[::-1]
    if x == x[::-1]:
        return True
    return False
x = str(input())
checked_palindrome(x)
 
if True:
    print("Yes")
else:
    print("No")  

