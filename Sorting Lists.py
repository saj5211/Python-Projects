aList = ['apple', 'cat','dog', 'banana']
def lessThan4(aList):
    result = []
    for e in aList:
        print result
        if len(e) >= 4:
            print result
            continue
        result.append(e)
        print result

    return result