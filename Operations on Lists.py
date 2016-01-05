## using lists iteratively 
#Techs = ['MIT', 'Cal Tech']
#Ivys = ['Harvard', 'Yale', 'Brown']
#
#Univs = [Techs, Ivys]
#Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]
#for e in Univs:
#    print('Univs contains')
#    print (e)
#    print('    which contains')
#    for u in e:
#        print('        ' + u)
#        
# to bring lists to the same level is called flattening ex flat = Techs + Ivys

#removing duplicates
L1 = [1,2,3,4]
L2 = [2,4,6,8]
def removeDups(L1,L2):
    L1Start = L1[:]
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
print (L1)