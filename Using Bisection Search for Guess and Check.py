# using bisection search for guess and check
x= 25
epsilon = 0.01 #the step size
low = 0.0
high =x
numGuesses = 0
ans = (high+low)/2.0
while (abs(ans**2-x))>= epsilon: #if true then too far apart from root
    print('low= '+ str(low) + ' high= ' + str(high) + ' ans= '+ str(ans)) 
    numGuesses +=1
    if ans**2 <x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
print ('numGuesses = ' +str(numGuesses))
print(str(ans) + ' is close to the square root of ' + str(x))