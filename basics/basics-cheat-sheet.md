# Module 1 Cheat Sheet: Python Basics

| Package/Method | Description | Code Example |
|----------------|-------------|--------------|
| **Comments** | Lines of text that are ignored by the Python interpreter when executing the code | `# This is a comment` |
| **Concatenation** | Combines (concatenates) strings.<br><br>**Syntax:**<br>`concatenated_string = string1 + string2`<br><br>**Example:**<br>`result = "Hello" + " John"` | |
| **Data Types** | - Integer<br>- Float<br>- Boolean<br>- String | `x = 7  # Integer Value`<br>`y = 12.4  # Float Value`<br>`is_valid = True  # Boolean Value`<br>`is_valid = False  # Boolean Value`<br>`F_Name = "John"  # String Value` |
| **Indexing** | Accesses character at a specific index. | `my_string = "Hello"`<br>`char = my_string[0]` |
| **len()** | Returns the length of a string.<br><br>**Syntax:**<br>`len(string_name)` | `my_string = "Hello"`<br>`length = len(my_string)` |
| **lower()** | Converts string to lowercase. | `my_string = "Hello"`<br>`lowercase_text = my_string.lower()` |
| **print()** | Prints the message or variable inside `()`. | `print("Hello, world")`<br>`print(a + b)` |
| **Python Operators** | - Addition (+): Adds two values together.<br>- Subtraction (-): Subtracts one value from another.<br>- Multiplication (*): Multiplies two values.<br>- Division (/): Divides one value by another, returns a float.<br>- Floor Division (//): Divides one value by another, returns the quotient as an integer.<br>- Modulo (%): Returns the remainder after division. | `x = 9`<br>`y = 4`<br>`result_add = x + y  # Addition`<br>`result_sub = x - y  # Subtraction`<br>`result_mul = x * y  # Multiplication`<br>`result_div = x / y  # Division`<br>`result_fdiv = x // y  # Floor Division`<br>`result_mod = x % y  # Modulo` |
| **replace()** | Replaces substrings. | `my_string = "Hello"`<br>`new_text = my_string.replace("Hello", "Hi")` |
| **Slicing** | Extracts a portion of the string.<br><br>**Syntax:**<br>`substring = string_name[start:end]` | `my_string = "Hello"`<br>`substring = my_string[0:5]` |
| **split()** | Splits string into a list based on a delimiter. | `my_string = "Hello"`<br>`split_text = my_string.split(",")` |
| **strip()** | Removes leading/trailing whitespace. | `my_string = " Hello "`<br>`trimmed = my_string.strip()` |
| **upper()** | Converts string to uppercase. | `my_string = "Hello"`<br>`uppercase_text = my_string.upper()` |
| **Variable Assignment** | Assigns a value to a variable.<br><br>**Syntax:**<br>`variable_name = value` | `name = "John"  # assigning John to variable name`<br>`x = 5  # assigning 5 to variable x` |