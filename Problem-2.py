def generate_odd_numbers(a):
    odd_numbers = []
    for i in range(1, 2 * a, 2):
        odd_numbers.append(i)
    return odd_numbers

a = 4
print(generate_odd_numbers(a))  
