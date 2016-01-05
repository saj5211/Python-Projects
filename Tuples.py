#Concatenation is adding two string together ex. print (t1+t2)
# Indexing is finding an object in a tuple ex print((t1+t2)[3])
# slicing is sperating strings ex ((t1+t2)[2:5])
# singleton t3 = ('five',) print(t1+t2+t3)
#[::2] used for returning odd tuples
#Manipulating Tuples
def findDivisors(n1, n2):
    """assumes that n1 and n2 are positive ints
       returns a tuple containing the common divisors of n1 and n2"""
    divisors = () # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors


divisors = findDivisors(20, 100)
total = 0
for d in divisors:
    total += d
print(total)