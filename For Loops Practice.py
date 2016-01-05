#Practice for for loops and Guess and Check

#1 printing out each character
#myStr = '6.00x'

#for char in myStr:
#    print char

#print 'done'

#2 printing the letter after the first letter 2x
#greeting = 'Hello!'
#count = 0

#for letter in greeting:
#    count += 1
#    if count % 2 == 0:
#        print letter 
#    print letter
#
#print 'done'

#3 fiding the amount of vowels and contenants in a sentence
#school = 'Massachusetts Institute of Technology'
#numVowels = 0
#numCons = 0
#
#for char in school:
#    if char == 'a' or char == 'e' or char == 'i' \
#       or char == 'o' or char == 'u':
#       numVowels += 1
#   elif char == 'o' or char == 'M':
#       print char
#   else:
#        numCons -= 1
#
#print 'numVowels is: ' + str(numVowels)
#print 'numCons is: ' + str(numCons) 

# For Loop Short statments practice

#1
#num = 10
#for num in range(5):
#    print num
#print num 

#2.
#divisor = 2
#for num in range(0, 10, 2):
#    print num/divisor 

#3.
#for variable in range(20):
#    if variable % 4 == 0:
#        print variable
#    if variable % 16 == 0:
#        print 'Foo!' 

#4.
#count = 0
#for letter in 'Snow!':
#    print 'Letter # ' + str(count) + ' is ' + str(letter)
#    count += 1
#    break
#print count 

# How to Calulate how many times a word occurs ina sequence of letter
#s = 'boobqbobbobbobobbobobobobo'
#numBob = 0
#l= len(s)
#for i in range(2,l):
#    if s[i-3]=='b' and s[i-2]=='o' and s[i-1]=='b':
#       numBob += 1   
#
#print 'Number of bobs: ' + str(numBob)

#how to find the longest alphabetical substring
#current_index = 1
#first_index = 0
#
#result_string = s[first_index]
#current_string = s[first_index]
#
#while current_index < len(s):
#    if ord(s[first_index]) <= ord(s[current_index]):
#        current_string += s[current_index]
#    elif ord(s[current_index]) < ord(s[first_index]):
#        current_string = s[current_index]
#
#    if len(current_string) > len(result_string):
#        result_string = current_string[:]
#
#    current_index += 1
#    first_index += 1
#
#
#print('Longest substring in alphabetical order is: ' + result_string)
