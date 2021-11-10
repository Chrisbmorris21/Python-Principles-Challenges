def only_ints(param1 , param2):
    
    condition1 = False
    condition2 = False
    
    if type(param1) == int:
        condition1 = True
    if type(param2) == int:
        condition2 = True

    if condition1 and condition2 == True:
        return True
    else:
        return False
    
only_ints(1, 2)
