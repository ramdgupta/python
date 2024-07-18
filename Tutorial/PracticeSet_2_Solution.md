```markdown
# Arithmetic Operators:

1. Create variables for two numbers and perform addition, subtraction, multiplication, division, and modulo (remainder) operations on them. Print the results.

```python
# Define variables
num1 = 10
num2 = 5

# Addition
addition = num1 + num2
print("Addition:", addition)

# Subtraction
subtraction = num1 - num2
print("Subtraction:", subtraction)

# Multiplication
multiplication = num1 * num2
print("Multiplication:", multiplication)

# Division
division = num1 / num2
print("Division:", division)

# Modulo (Remainder)
modulo = num1 % num2
print("Modulo:", modulo)
```

2. Ask the user to input two numbers and a choice of operation (+, -, , /, %). Perform the selected operation and display the result.

```python
# Input numbers and operation choice
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, , /, %): ")

# Perform operation based on choice
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
elif operation == '%':
    result = num1 % num2
else:
    print("Invalid operation")

print("Result:", result)
```

# Prime and Non-Prime Number Generator:

1. Write a function that receives a number as input and determines whether it's prime or not. Print "Prime" for prime numbers and "Not prime" for non-prime numbers.

```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime")
else:
    print("Not prime")
```

2. Create a list of prime numbers between 1 and 100 using a loop.

```python
prime_numbers = [num for num in range(1, 101) if is_prime(num)]
print("Prime numbers between 1 and 100:", prime_numbers)
```

# Composite Number Generation:

1. Define a function that generates and returns a list of composite numbers within a specified range.

```python
def generate_composite_numbers(start, end):
    composite_numbers = []
    for num in range(start, end + 1):
        if not is_prime(num):
            composite_numbers.append(num)
    return composite_numbers

print("Composite numbers between 20 and 50:", generate_composite_numbers(20, 50))
```

2. Create a set of composite numbers between 20 and 50.

```python
composite_set = set(generate_composite_numbers(20, 50))
print("Composite numbers set between 20 and 50:", composite_set)
```

# For Loop:

1. Iterate through a list of names and print a greeting for each name.

```python
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Hello,", name)
```

2. Print even numbers from 1 to 20 using a for loop.

```python
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print("Even numbers from 1 to 20:", even_numbers)
```

3. Calculate the factorial of a given number using a for loop.

```python
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, ":", factorial)
```

# List, Set, and Dictionary:

1. Create a list of 5 fruits and print the second and fourth fruits.

```python
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
print("Second fruit:", fruits[1])
print("Fourth fruit:", fruits[3])
```

2. Remove a specific fruit from the list and print the updated list.

```python
fruits.remove("Banana")
print("Updated list of fruits:", fruits)
```

3. Create a set of colors and add a new color to it.

```python
colors_set = {"Red", "Green", "Blue"}
colors_set.add("Yellow")
print("Updated set of colors:", colors_set)
```

4. Check if a given color exists in the set.

```python
color = input("Enter a color to check: ")
if color in colors_set:
    print(color, "exists in the set")
else:
    print(color, "does not exist in the set")
```

5. Create a dictionary to store student scores, with names as keys and scores as values.

```python
student_scores = {"Alice": 90, "Bob": 85, "Charlie": 95}
```

6. Print the scores of all students.

```python
print("Student scores:")
for name, score in student_scores.items():
    print(name, ":", score)
```

7. Find the student with the highest score.

```python
highest_score_student = max(student_scores, key=student_scores.get)
print("Student with the highest score:", highest_score_student)
```
```