def my_function(**kwargs):
    print(kwargs)
    print(f'My name is {kwargs['first_name']} {kwargs['last_name']} . I am {kwargs['age']} years old. I live in {kwargs['address']}')

my_function(first_name = 'Rahim', last_name = 'khan', age = 26, address = 'Dhaka')
