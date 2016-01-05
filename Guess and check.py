# finding cube root with guess and check 
x = int(raw_input('Enter an Interger: ' ))
ans = 0
#while ans**3 <x: postive only
while ans**3 <abs(x):
        ans = ans + 1
##if ans**3 !=x: positive only
if ans**3 !=abs(x):
        print(str(x) + ' is not a perfect cube')
else: 
    if x<0:  #negative only
            ans = -ans #negative only
    print ('Cube root of ' + str(x) + ' is ' + str(ans))
        