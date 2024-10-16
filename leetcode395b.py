
def minimumAddedInteger(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    result = 1000
    

            # true/false
    def works(i):
        chances = 0
        
        diff = nums2[0] - nums1[i]
        j = i
        while j < len(nums1) - 1:
            if j - i >= len(nums2):
                break
            if nums2[j - i] - nums1[j] != diff:
                chances += 1
                i += 1
                if chances > 2:
                    return False
                
            j += 1
        if len(nums1) < len(nums2) + i:
            return False
        return True
    
    # for third
    if works(2):
        result = min(result, nums2[0] - nums1[2] )
        
    # for second
    if works(1):
        result = min(result, nums2[0] - nums1[1])
    
    if works(0):
        result = min(result, nums2[0] - nums1[0])
    
    return result
    

nums1 = [7,9,1,4]
nums2 = [0,8]

print(minimumAddedInteger(nums1, nums2))