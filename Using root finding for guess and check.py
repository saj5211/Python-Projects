#using root finding to make guess and check more efficient
epsilon = 0.01
y = 12345
guess = y/2.0

while abs(guess*guess - y)>=epsilon:
        guess = guess - (((guess**2)-y)/(2*guess))
        print(guess)
print('Square root of' + str(y) + ' is about ' +str(guess))

