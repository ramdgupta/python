```markdown
# Practice Set: Generating Composite Numbers

## 1. Using a Loop and Divisibility Check

```python
def generate_composite_numbers(start, end):
    """Generates a set of composite numbers within a given range."""
    composite_numbers = set()
    
    # Check for divisibility by 2 first (even numbers are composite except 2)
    for num in range(start, end + 1, 2):
        if num > 2:
            composite_numbers.add(num)
    
    # Check for divisibility by odd numbers from 3 to the square root of the end number
    for num in range(start, end + 1):
        if num > 1 and num % 2 != 0:
            is_composite = False
            for i in range(3, int(num**0.5) + 1, 2):  # Check only odd divisors
                if num % i == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(num)
    
    return composite_numbers

# Example usage
start_range = 20
end_range = 50
composite_set = generate_composite_numbers(start_range, end_range)

print("Composite numbers between", start_range, "and", end_range, ":", composite_set)
```

### Explanation

This function defines a loop that iterates through the given range.
- First, it checks for even numbers and adds them to the composite_numbers set (except 2, which is prime).
- Then, it loops through odd numbers only, checking for divisibility by odd numbers from 3 to the square root of the current number (efficiently avoiding unnecessary checks).
- If a divisor is found, the number is marked as composite and added to the set.

## 2. Using List Comprehension

```python
def generate_composite_numbers_list(start, end):
    """Generates a list of composite numbers within a given range."""
    composite_numbers = [num for num in range(start, end + 1) if (num > 2 and (num % 2 == 0 or any(num % i == 0 for i in range(3, int(num**0.5) + 1, 2))))]
    return composite_numbers

# Example usage
start_range = 20
end_range = 50
composite_list = generate_composite_numbers_list(start_range, end_range)

print("Composite numbers between", start_range, "and", end_range, ":", composite_list)
```

### Explanation

This function uses list comprehension to create a list of composite numbers.
- It iterates through the range and checks for the following conditions:
  - The number is greater than 2.
  - It's either even or divisible by any odd number from 3 to the square root (using a nested generator expression).
- If both conditions are met, the number is added to the composite_numbers list.

These are two ways to generate composite numbers. Choose the approach that best suits your needs and coding style.
```
```