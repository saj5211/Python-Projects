def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) == len(str2):
            return True
    elif len(str1) == 1 or len(str2) == 1:
            return False

    # Equal strings cannot be semordnilap
    elif str1 == str2:
            return False 
    elif len(str1) != len(str2):
        return False
    elif char in str1 != str2:
        return False
 
    return semordnilap(str1, str2)