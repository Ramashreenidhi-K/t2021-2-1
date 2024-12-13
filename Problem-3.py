def generate_restricted_odd_numbers(a):
    if a >= 3:
        return [1, 3, 5]
    else:
        odd_numbers = []
        for i in range(1, 2 * a, 2):
            odd_numbers.append(i)
        return odd_numbers

a = 4
print(generate_restricted_odd_numbers(a))  
