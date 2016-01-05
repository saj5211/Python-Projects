#succesive addition to solve for multiplication problems
def iterMul(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

#recursive way
def  recurMul(a,b):
    if b ==1:
        return a
    else: 
        return a + recurMul(a, b-1)
