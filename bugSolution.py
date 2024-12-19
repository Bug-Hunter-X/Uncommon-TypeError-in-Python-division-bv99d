def function_with_improved_error_handling(a, b):
    try:
        if isinstance(b, (int, float)):
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = a / b
            return result
        else:
            raise TypeError("Unsupported operand type(s) for /: 'int' and '"+ str(type(b).__name__) +"'.")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

#Demonstrate improved error handling
result1 = function_with_improved_error_handling(10, 0)
print(result1)
result2 = function_with_improved_error_handling(10, "hello")
print(result2)
result3 = function_with_improved_error_handling(10, 5)
print(result3)