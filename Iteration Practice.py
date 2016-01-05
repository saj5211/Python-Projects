# Practise on iteration
#1.
#num = 0
#while num <= 5:
#    print num
#    num += 1
#print "Outside of loop"
#print num 

#2.
#numberOfLoops = 0
#numberOfApples = 2
#while numberOfLoops < 10:
#    numberOfApples *= 2
#    numberOfApples += numberOfLoops
#    numberOfLoops -= 1
#print "Number of apples: " + str(numberOfApples)

#3.
#num = 10
#while num > 3:
#    num -= 1
#    print num 

# 4. Uses break
#num = 10
#while True:
#    if num < 7:
#        print 'Breaking out of loop'
#        break
#    print num
#    num -= 1
#print 'Outside of loop' 

## 5.
num = 100
while not False:
    if num < 0:
        break
print 'num is: ' + str(num) 