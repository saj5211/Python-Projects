# using approximation for guess and check
x= 25
epsilon = 1 #the step size
step = 1
numGuesses = 0
ans = 0.0

while (abs(ans**2-x))>= epsilon and ans <=x:
    ans =+ step
    numGuesses +=1
print ('numGuesses = ' +str(numGuesses))
if abs(ans**2-x) >= epsilon:
    print ('failed on square root of ' +str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))