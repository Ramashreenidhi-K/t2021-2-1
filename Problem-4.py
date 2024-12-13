def count_multiples(numbers):
    count_dict = {i: 0 for i in range(1, 10)}
    
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                count_dict[i] += 1
                
    return count_dict

numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(numbers))
