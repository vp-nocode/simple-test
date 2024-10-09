def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def check(number):
    return number % 2 == 0

def divide_zero(a, b):
   if b == 0:
       raise ValueError('Division by 0 error')
   return a / b

def mod(a, b):
    if b == 0:
        raise ValueError('Division by 0 error')
    return a % b
