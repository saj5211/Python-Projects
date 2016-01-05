#Dictionary
# Syntax
#monthNumbers = {'Jan':1} Curly braces tells us that it is a dictionary, the text is the key followed by a colon and value
#the comma seperates one pair from another
#Ex.
monthNumbers = {'Jan':1, 'Feb':2,
'Mar':3, 
1:'Jan', 2:'Feb', 3:'Mar'}

#Insertion: Inserting keys and values
monthNumbers['Apr'] = 4

# Iteration

collect = [ ]
for e in monthNumbers:
        collect.append(e)
        
# complex keys
myDict = {(1,2): ' twelve',
(1,3):'thirteen'}

myDict[(1,2)]