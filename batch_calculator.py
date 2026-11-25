"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    operation, a_text, b_text = map(str.strip, (operation, a_text, b_text))

    ops = {
    "add" : add,
    "subtract" : subtract,
    "multiply" : multiply,
    "divide" : divide 
    }

    if operation not in ops:
        return("ERROR", "", "UNKNOWN_OPERATION")

    try:
        a, b = float(a_text), float(b_text)
    except ValueError:
        return ("ERROR", "", "INVALID_NUMBER")

    try:
        result = ops.get(operation)(a, b)
    except ZeroDivisionError:
        return ("ERROR", "", "DIVISION_BY_ZERO")

    return ("OK", result, "")
    

    