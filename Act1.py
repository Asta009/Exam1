def missing_int(A):

    positive_integers = set()
    for num in A:
        if num > 0:
            positive_integers.add(num)
    
    missing = 1
    while missing in positive_integers:
        missing += 1
    
    return missing

print(missing_int([1, 3, 6, 4, 1, 2]))  
print(missing_int([1, 2, 3]))            
print(missing_int([-1, -1, -1, -5]))    
print(missing_int([1, 3, 6, 4, 1, 7, 8, 10]))  