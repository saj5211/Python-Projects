d = {0: 0, 1: 0, 10: 0, 5: 1, 9: 0}

def keysWithValue(aDict, target):
    ans = []
    #for k, v in aDict.iteritems():
    for k, v in aDict.items():
        if v == target:
          ans.append(k)
    return sorted(ans)

print(keysWithValue(d, 0))