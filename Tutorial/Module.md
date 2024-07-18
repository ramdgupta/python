Sure! Below is an overview of common operations involving modules in Python, along with a set of practice exercises:

### Operations on Modules:

1. **Importing Modules**:
   - Modules are files containing Python code that can be imported into other Python scripts.
   ```python
   import math
   ```

2. **Using Module Attributes and Functions**:
   - After importing a module, its attributes and functions can be accessed using dot notation.
   ```python
   print(math.pi)
   print(math.sqrt(25))
   ```

3. **Renaming Modules**:
   - Modules can be imported with an alias for convenience.
   ```python
   import datetime as dt
   ```

4. **Importing Specific Items**:
   - Specific items from a module can be imported instead of the whole module.
   ```python
   from random import randint
   ```

5. **Creating Modules**:
   - Modules can also be user-created Python files containing functions, classes, or variables that can be imported into other scripts.
   ```python
   # mymodule.py
   def greet(name):
       return f"Hello, {name}!"
   ```

### Practice Set for Modules:

1. **Importing and Using Modules**:
   - Import the `math` module and use it to find the square root of a number.
   - Import the `random` module and use it to generate a random number between 1 and 10.

2. **Renaming Modules**:
   - Import the `datetime` module with the alias `dt` and use it to get the current date and time.
   - Import the `statistics` module with the alias `stats` and use it to find the mean of a list of numbers.

3. **Importing Specific Items**:
   - Import the `randint` function from the `random` module and use it to generate a random integer between 1 and 100.

4. **Creating and Importing Custom Modules**:
   - Create a Python file named `mymodule.py` with a function `greet(name)` that returns a greeting message.
   - Import the `greet` function from `mymodule` and use it to greet a friend.

These exercises cover a variety of operations and concepts related to modules in Python and should provide good practice for beginners.