# Beginner Python Knowledge:

1. Variables and Data Types:

   - Create variables to store your name, age, and favorite color and print them:
     ```python
     name = "Ram Dulare"
     age = "40"
     favColor = "Black"
     print(name, age, favColor)
     ```

   - Create variables of different data types and perform operations on them:
     ```python
     myPet = "ISAR"
     myId = 5
     myAge = 40
     divisible = 10 / 5
     reminder = 9 % 4
     mySalary = 5.5
     haveChild = True
     ```

   - Create a list of your favorite foods and print each item:
     ```python
     myList = ["Dal", "Roti", "Rice", "Paratha", "Halwa"]
     for fav in myList:
         print(fav)
     ```

   - Print the name in a formatted string:
     ```python
     name = input("Enter your name: ")
     print(f"Hello {name}")
     ```

   - Print age as an integer:
     ```python
     age = input("Enter your age: ")
     print(f"Hello {name} your age is {int(age)}")
     ```

   - Check if a number is even or odd:
     ```python
     num = int(input("Enter the number: "))
     if num % 2 == 0:
         print(f"The number {num} is Even")
     else:
         print(f"The number {num} is Odd")
     ```

   - Check eligibility age for voting:
     ```python
     if age > 18:
         print(f"Your age {age} is greater than 18, so you are eligible to vote")
     elif age == 18:
         print(f"Your age {age} is equal to 18, so you are eligible to vote")
     else:
         print(f"Your age {age} is below 18, so you are not eligible to vote")
     ```

# Intermediate Python Knowledge:

1. Functions:

   - Define a function to add two numbers:
     ```python
     def add_num(a, b):
         return a + b
     ```

   - Define a function to calculate the area of a rectangle:
     ```python
     def rec_area(l, w):
         return l * w
     ```

   - Define a function to determine if a given number is prime:
     ```python
     def check_no(num):
         if num % 2 == 0:
             return "This is prime no"
         else:
             return "This is not a prime no"
     ```

2. Lists and Tuples:

   - Use list comprehensions to generate a list of even numbers between 1 and 20:
     ```python
     even_numbers = [x for x in range(1, 21) if x % 2 == 0]
     print(even_numbers)
     ```

   - Create a list of tuples, where each tuple holds a student's name and grade:
     ```python
     students = [("ram", 85), ("shyam", 65), ("gyan", 95)]
     for student in students:
         name, grade = student  # Unpack tuple into variables name and grade
         print(f"Student: {name}, Grade: {grade}")
     ```

   - Sort a list of names in alphabetical order:
     ```python
     names = ["Alice", "Bob", "Ram", "Ajay", "Vinod", "Gyan"]
     names = sorted(names)
     print(names)
     ```

3. Dictionaries and Sets:

   - Create a dictionary to store information about a book (title, author, year published):
     ```python
     book = {"title": "Shiva Trilogy", "author": "Varun Goyal", "year": 2024, "published": True}
     print(book["title"])
     ```

   - Use a set to store unique elements from a list of numbers:
     ```python
     num_set = {1, 12, 15, 18, 2, 4, 5, 2, 3, 12, 15, 1, 2}
     print(num_set)
     ```

   - Create a dictionary whose keys are country names and values are their corresponding capital cities:
     ```python
     capital = {"india": "Delhi", "USA": "Washington", "Australia": "Sydney", "Nepal": "Kathmandu"}
     ```

# Modules and Packages:

- Import the `math` module and use functions like `sqrt()` and `pi`:
  ```python
  import math
  math.floor(math.sqrt(2))
  math.pi
