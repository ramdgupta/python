Certainly! Here's an overview of common operations on files in Python along with a set of practice exercises:

### Operations on Files:

1. **Opening Files**:
   - Files can be opened using the built-in `open()` function, specifying the file path and mode (read, write, append, etc.).
   ```python
   file = open('filename.txt', 'r')
   ```

2. **Reading from Files**:
   - File contents can be read using various methods like `read()`, `readline()`, or `readlines()`.
   ```python
   content = file.read()
   line = file.readline()
   lines = file.readlines()
   ```

3. **Writing to Files**:
   - Files can be written using methods like `write()` or `writelines()`.
   ```python
   file.write('Hello, World!\n')
   file.writelines(['Line 1\n', 'Line 2\n'])
   ```

4. **Closing Files**:
   - After operations, files should be closed using the `close()` method.
   ```python
   file.close()
   ```

5. **Using Context Managers**:
   - The `with` statement can be used to automatically close files after use.
   ```python
   with open('filename.txt', 'r') as file:
       content = file.read()
   ```

6. **File Modes**:
   - Files can be opened in different modes such as read (`'r'`), write (`'w'`), append (`'a'`), binary read (`'rb'`), binary write (`'wb'`), etc.

### Practice Set for Files:

1. **Creating and Writing to Files**:
   - Create a new text file named "sample.txt" and write some text into it.

2. **Reading from Files**:
   - Open the "sample.txt" file and read its contents using the `read()` method.
   - Open the "sample.txt" file and read its contents line by line using the `readline()` method.

3. **Appending to Files**:
   - Open the "sample.txt" file in append mode and add some additional text to it.

4. **Reading and Writing with Context Managers**:
   - Use a context manager to open the "sample.txt" file and read its contents.
   - Use a context manager to open the "sample.txt" file and append some text to it.

5. **File Modes**:
   - Open the "sample.txt" file in write mode (`'w'`) and write some text into it.
   - Open the "sample.txt" file in binary write mode (`'wb'`) and write some binary data into it.

These exercises cover a variety of operations and concepts related to working with files in Python and should provide good practice for beginners.