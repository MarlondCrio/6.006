def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    genCount= 0
    #gencount is like length of increasing stuffs
    lengths = []
    previous = A[0]
    place = 0
    for elements in A:
    #Iterates through list    
        place += 1
        if elements >  previous :
            #checks if element is bigger or not
            previous = elements
            genCount += 1


            if place == len(A):
                #for the last digit in case something happens
                genCount += 1
                lengths.append(genCount)
               
        elif (elements <= previous and (place != 1)):
            #if it isnt bigger it starts a new list
            previous = elements

            genCount += 1 
            lengths.append(genCount)


            genCount = 0
    
    count = 0 
    
    Max = max(lengths)
    #finds max length of increasing numbers then
    #Finds how many times it appears
    for elements in lengths:
        if  elements == Max:
            count += 1
    
    return count


