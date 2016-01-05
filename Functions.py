#Functions
#Syntax of Functions
# def <functionname> (<functionparameters>):
    #<functionbody>

#Simple example of defining function
#def Max (x,y):
#     if x < y:
#        return x
#     else: 
#        return y
#z = max(10,12)
#print(z)

#Example
x = float(raw_input('Enter a number: '))
p = int(raw_input('Enter an integer power: '))
result =1

for turn in range (p):
    print('iteration: ' + str(turn) + 'current result: ' + str(result))
    result= result * x

def iterativePower(x,p):
    result =1
    for turn in range (p):
        print('iteration: ' + str(turn) + 'current result: ' + str(result))
        result= result * x
    return result