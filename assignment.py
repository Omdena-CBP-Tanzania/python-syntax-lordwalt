def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    
    return f"My name is {name} and I am {age} years old."

# Example
name = "Alice"
age = 24
result = format_string(name, age)
print(result)
pass

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

# Example
number = 12
result = conditional_check(number)
print(result)
pass

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Example
n = 10
result = loop_sum(n)
print(result)
pass

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return (total, maximum, minimum)

# Example
numbers = [1, 2, 3, 4, 5]
result = list_operations(numbers)
print(result)
pass

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    students_dict = { "John" : 95, "Alan" : 77, "Steven" : 87, "Janet" : 91, "Suzan" : 80 }
    
    return [name for name, score in students_dict.items() if score > 80]

# Example
list1 = { "John" : 95, "Alan" : 77, "Steven" : 87, "Janet" : 91, "Suzan" : 80 }
print(dict_operations(list1))
pass

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    return set(list1) & set(list2)

# Example
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = set_operations(list1, list2)
print(result)
pass

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b
    return {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}

# Example 
a = 25
b = 8
result = arithmetic_ops(a, b)
print(result)
pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    x = True
    y = False
    return {"and": x and y, "or": x or y, "not x": not x, "not y": not y}

# Example
x= True
y= False
result = logical_ops(x, y)
print(result)
pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    a = 10
    b = 4
    return {"and": a & b, "or": a | b, "xor": a ^ b, "left shift": a << 2, "right shift": a >> 2}

# Example
a = 10
b = 4
result = bitwise_ops(a, b)
print(result)
pass