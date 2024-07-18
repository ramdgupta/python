## Detailed Practice Set for Python Prerequisites for Generative AI

This practice set provides detailed explanations and examples to reinforce your understanding of fundamental Python concepts crucial for Generative AI:

**1. Variables and Data Types:**

**Explanation:** Variables store information in your program. They have a specific data type that determines the type of data they can hold.

**Practice:**

1. **Create variables:**

   ```python
   name = "John Doe"  # string
   age = 30          # integer
   has_coding_experience = True  # boolean
   hobbies = ["coding", "reading", "music"]  # list
   programming_skills = {"Python": "Intermediate", "Java": "Beginner"}  # dictionary
   ```

2. **Print information:**

   ```python
   print("Name:", name, type(name))
   print("Age:", age, type(age))
   print("Has coding experience:", has_coding_experience, type(has_coding_experience))
   print("Hobbies:", hobbies, type(hobbies))
   print("Programming skills:", programming_skills, type(programming_skills))
   ```

3. **Perform operations:**

   ```python
   future_age = age + 5
   print("Future age:", future_age)

   remainder = age % 2
   print("Remainder when divided by 2:", remainder)
   ```

**2. Operators and Control Flow:**

**Explanation:** Operators perform calculations and comparisons, while control flow statements dictate how your program executes based on certain conditions.

**Practice:**

1. **User input:**

   ```python
   number = int(input("Enter a number: "))
   ```

2. **Even/Odd check:**

   ```python
   if number % 2 == 0:
       print(number, "is even.")
   else:
       print(number, "is odd.")
   ```

3. **For loop:**

   ```python
   for hobby in hobbies:
       print(hobby)
   ```

4. **While loop:**

   ```python
   total_sum = 0
   while True:
       entered_number = int(input("Enter a number (negative to stop): "))
       if entered_number < 0:
           break
       total_sum += entered_number
   print("Sum of entered numbers:", total_sum)
   ```

**3. Functions:**

**Explanation:** Functions are reusable blocks of code that perform specific tasks. They can take inputs (arguments) and return outputs (values).

**Practice:**

1. **Greet function:**

   ```python
   def greet(name):
       print("Hello,", name, "!")

   greet("Alice")  # Calling the function
   ```

2. **Area calculation function:**

   ```python
   def calculate_area(length, width):
       return length * width

   rectangle_area = calculate_area(5, 3)
   print("Rectangle area:", rectangle_area)
   ```

3. **Prime number check function:**

   ```python
   def is_prime(num):
       if num <= 1:
           return False
       for i in range(2, int(num**0.5) + 1):
           if num % i == 0:
               return False
       return True

   if is_prime(7):
       print("7 is prime.")
   else:
       print("7 is not prime.")
   ```

**4. Lists and Tuples:**

**Explanation:** Lists are ordered, mutable collections of items. Tuples are similar but immutable (cannot be changed after creation).

**Practice:**

1. **List operations:**

   ```python
   numbers = list(range(1, 11))  # Create list using range() function

   print("First element:", numbers[0])
   print("Third element:", numbers[2])
   print("Last element:", numbers[-1])

   doubled_numbers = [num * 2 for num in numbers]  # List comprehension for multiplication
   print("Doubled numbers:", doubled_numbers)
   ```

2. **Tuples:**

   ```python
   favorite_color, movie_genre, author = "Blue", "Sci-fi", "Isaac Asimov"

   print("Favorite color:", favorite_color)
   print("Movie genre:", movie_genre[1:3])  # Slicing to get "Sci"
   ```

**5. Sets and Dictionaries:**

**Explanation:** Sets store unique elements and are unordered. Dictionaries store key-value pairs, allowing efficient data retrieval using keys