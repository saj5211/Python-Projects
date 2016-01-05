## Lec 2.6
## Conditional

##x = int(raw_input('Enter an Integer: '))
##if x%2 == 0:
 ##       print (' ')
##        print ('Even')
##else:
 ##       print (' ')
##        print('Odd')
##print ('done with conditional')

##Nested Conditionals

##x = int(raw_input('Enter an Integer: '))
##if x%2 ==0:
##        if x%2 ==0:
##            print('Divisble by 2 and 3')
##        else:
##            print('Divisble by 2 but not 3')
##elif x%3 == 0:
##        print('Dvisible by 3 and not by 2')
##else:
##        print('Not divisible by 2 or 3')

## Compound Booleans
x = int(raw_input('Enter an Integer: '))   
if x<y and x<z:
        print ('x is leat')
elif y<z:
        print('y is least')
else:
        print('z is least')