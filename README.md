# Solutions for Problems by Ramashreenidhi k
## Program Language usage : Python
## Introduction


This repository contains solutions for 4 problems: 

1. **Problem-1: Simple Calculator Using Class**
2. **Problem-2: Generate Odd Numbers Series**
3. **Problem-3: Generate Restricted Odd Numbers Series**
4. **Problem-4: Count Multiples in Dictionary**

## **Problem-1: Simple Calculator Using Class**
### **Code:**

```python
class Calculator:
    def __init__(self, a, b, operation):
        self.a = a  # First number
        self.b = b  # Second number
        self.operation = operation 

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b  # Perform addition
        elif self.operation == 'subtraction':
            return self.a - self.b  # Perform subtraction
        elif self.operation == 'multiplication':
            return self.a * self.b  # Perform multiplication
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b  # Perform division
            else:
                return "Error: Division by zero"  #  division by zero error
        else:
            return "Invalid operation"  # error message if wrong operation other than given options
```
## Problem 2: Generate Odd Numbers Series

### **Code:**
```python
def generate_odd_numbers(a):
    odd_numbers = []
    for i in range(1, 2 * a, 2):  # Generate odd numbers 
        odd_numbers.append(i)
    return odd_numbers

a = 4
print(generate_odd_numbers(a)) 
```
## Problem 3: Generate Restricted Odd Numbers Series
### **Code:**
```python
def generate_restricted_odd_numbers(a):
    if a >= 3:
        return [1, 3, 5]  # Return  the first three odd numbers if 'a' is 3 or more
    else:
        odd_numbers = []
        for i in range(1, 2 * a, 2): 
            odd_numbers.append(i)
        return odd_numbers

a = 4
print(generate_restricted_odd_numbers(a)) 
```
## Problem 4: Count Multiples in Dictionary
### **Code:**
```python
def count_multiples(numbers):
    count_dict = {i: 0 for i in range(1, 10)}  # Initialize the dictionary for counting 
    
    for num in numbers:
        for i in range(1, 10):  # Checking the divisibility 
            if num % i == 0:
                count_dict[i] += 1
                
    return count_dict

numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(numbers))  
```


