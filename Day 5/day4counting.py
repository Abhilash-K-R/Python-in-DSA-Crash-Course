# counting the number of times each character appears in a string              
# leetcode 387. First Unique Character in a String                                            

def counting(s):
    d = {}
    for c in s:
        if c in d:
            d[c] = d.get(c , 0) + 1
        else:
            d[c] = 1
    return d

print(counting("aaabcbb"))