Meta-programming in Python refers to the ability of a program to manipulate or generate code dynamically during runtime. This involves using features like decorators, metaclasses, and introspection. Below is an overview of common operations involving meta-programming in Python, along with a set of practice exercises:

### Operations on Meta-Programming:

1. **Decorators**:
   - Decorators are a form of meta-programming that allows you to modify the behavior of functions or methods dynamically.
   ```python
   def my_decorator(func):
       def wrapper(*args, **kwargs):
           print("Something is happening before the function is called.")
           result = func(*args, **kwargs)
           print("Something is happening after the function is called.")
           return result
       return wrapper

   @my_decorator
   def say_hello():
       print("Hello!")

   say_hello()
   ```

2. **Metaclasses**:
   - Metaclasses are classes for classes. They allow you to customize the creation and behavior of classes.
   ```python
   class MyMeta(type):
       def __new__(cls, name, bases, dct):
           dct['new_attribute'] = 42
           return super().__new__(cls, name, bases, dct)

   class MyClass(metaclass=MyMeta):
       pass

   obj = MyClass()
   print(obj.new_attribute)
   ```

3. **Introspection**:
   - Introspection allows you to examine the properties and methods of objects at runtime.
   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

   person = Person("Alice", 30)

   print(hasattr(person, 'name'))  # Check if 'name' attribute exists
   print(getattr(person, 'age'))   # Get the value of 'age' attribute
   ```

4. **Dynamic Code Execution**:
   - Python provides functions like `exec()` and `eval()` for dynamically executing code or evaluating expressions.
   ```python
   x = 10
   exec('print(x + 5)')  # Dynamically execute code
   result = eval('x * 2')  # Dynamically evaluate expression
   print(result)
   ```

### Practice Set for Meta-Programming:

1. **Decorators**:
   - Create a decorator called `log_function_call` that logs the function name and its arguments before and after the function call.
   - Apply the `log_function_call` decorator to a sample function and observe the logs.

2. **Metaclasses**:
   - Define a metaclass called `CustomMeta` that adds a class variable `meta_attribute` to any class it creates.
   - Create a class using the metaclass `CustomMeta` and print the value of `meta_attribute`.

3. **Introspection**:
   - Create a class `Book` with attributes `title` and `author`.
   - Use introspection to check if the `Book` class has an attribute named `author` and print its value.

4. **Dynamic Code Execution**:
   - Write a dynamic code that generates a function to calculate the square of a number.
   - Use the generated function to calculate the square of a given number.

5. **Practical Use Case**:
   - Write a decorator called `validate_arguments` that checks if the arguments passed to a function meet certain criteria.
   - Apply the `validate_arguments` decorator to a function that performs a calculation.

These exercises cover various aspects of meta-programming in Python and should provide good practice for those interested in exploring dynamic and advanced programming features.