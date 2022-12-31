def checked_palindrome(x):
    """
       Checks whether string is palindrome or not
    """  
    x == x[::-1]
    if x == x[::-1]:
        print ("True")
    else:
        print ("False")
x = str(input())
checked_palindrome (x)
