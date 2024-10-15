def find_key(nums):
    # Getting num length
    numLength = len(str(nums[0]))
    
    # Var
    i = 0 
    answer = ""
    
    # Try while i < numLength to get all numbers
    while i < numLength:
            
        # Var
        j = 0
        array = []
        
        # Try while j < numLength to catch the numbers of sequence
        while j < numLength:
            array.append(str(nums[j])[i])
            j = j + 1
            
        # Var
        k = 0
        
        # Try while k < 10 to find the number which repeat just once on sequence
        while k < 10:
            if array.count(str(k)) == 1:
                answer = answer + str(k)
                break
            k = k + 1   
            
        i = i + 1
        
    return answer