word = "dabdcbdcdcd"
k = 2

countdict = dict()

for char in word:
    countdict[char] = countdict.get(char, 0) + 1

def small_diff(mystring, i, j):
    return abs(countdict[mystring[i]] - countdict[mystring[j]]) <= k

# can memoize
# min number needed for a substring.
def dp(mystring, delete_so_far):
    print(mystring)
    print("delete so far: ", delete_so_far)
    print(countdict)
    mylen = len(mystring)
    if mylen == 2:
        if small_diff(mystring, 0, 1):
            return delete_so_far
        else:
            return float("-inf")
        
    if mylen == 3:
        if small_diff(mystring, 0, 1) and small_diff(mystring, 1, 2):
            return delete_so_far
        
        countdict[mystring[0]] = countdict.get(mystring[0]) - 1
        res1 = dp(mystring[1:], delete_so_far + 1)
        countdict[mystring[0]] = countdict.get(mystring[0]) + 1
        
        countdict[mystring[1]] = countdict.get(mystring[1]) - 1
        res2 = dp(mystring[:1] + mystring[2:], delete_so_far + 1)
        countdict[mystring[1]] = countdict.get(mystring[1]) + 1
        
        countdict[mystring[2]] = countdict.get(mystring[2]) - 1
        res3 = dp(mystring[:2], delete_so_far + 1)
        countdict[mystring[2]] = countdict.get(mystring[2]) + 1
        
        return min(res1, res2, res3)
    
    # mylen 3 and up
    # just find first problem 
    for i in range(mylen - 1):
        if not small_diff(mystring, i, i + 1):
            print("not small diff for i: ", i)
            
            countdict[mystring[i]] = countdict.get(mystring[i]) - 1
            res1 = dp(mystring[:i] + mystring[i + 1:], delete_so_far + 1)
            countdict[mystring[i]] = countdict.get(mystring[i]) + 1
            
            countdict[mystring[i + 1]] = countdict.get(mystring[i + 1]) - 1
            res2 = dp(mystring[:i + 1] + mystring[i + 2:], delete_so_far + 1)
            countdict[mystring[i + 1]] = countdict.get(mystring[i + 1]) + 1
            
            countdict[mystring[i]] = countdict.get(mystring[i]) - 1
            countdict[mystring[i + 1]] = countdict.get(mystring[i + 1]) - 1
            res3 = dp(mystring[:i] + mystring[i+ 2:], delete_so_far + 2)
            countdict[mystring[i]] = countdict.get(mystring[i]) + 1
            countdict[mystring[i + 1]] = countdict.get(mystring[i + 1]) + 1
            if res1 == 1:
                print("problem for i: ", i)
            print(res1, res2, res3)
            return min(res1, res2, res3)
    return delete_so_far
    
final = dp(word, 0)
print("final result: ", final)
