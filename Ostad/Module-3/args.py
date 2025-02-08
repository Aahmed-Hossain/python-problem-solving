def addition(*args):
    print(args) # args return as tuple
    return sum(args)

result = addition(1,3, 4, 5, 6)
print(result)
