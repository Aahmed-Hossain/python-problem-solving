# Function have two types (1) built in - input(), print(), ... (2) user defined functions - which may have input but must have output.

# 1. No input no return
def my_first_function():
    a = 6
    b = 7
    print(a + b)
my_first_function()

# 2. input , no return
def add_two_numbers(a, b): #a,b argument
    print(f'Addition: {a} + {b}')
    print(a - b)
add_two_numbers(5, 5) # parameters

# 3. input ,  return
def multiply_two_numbers(a,b):
    return a*b
result = multiply_two_numbers(6, 9)
print(result)

# 4. No input, return
def hello():
    return 'Hello'
greetings = hello()
print(greetings)
