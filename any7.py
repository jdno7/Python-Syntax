def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE 
    for el in nums:
        #print (type(el))
        if el == 7:
            return (True)
            #break
       
    return (False)

print(any7([1, 2, 7, 4, 5]))
print(any7([1, 2, 4, 5]))

