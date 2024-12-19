def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

# This error handling is not enough. What if 'b' is a string?
result = function_with_uncommon_error(10, "hello")
print(result)  #This will result in an error: TypeError: unsupported operand type(s) for /: 'int' and 'str'