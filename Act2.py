def find_divisible(a, b, k):
    count = 0
    for num in range(a, b + 1):
        if num % k == 0:
            count += 1
    
    return count

print(find_divisible(6, 11, 2))  
print(find_divisible(0, 11, 2))  