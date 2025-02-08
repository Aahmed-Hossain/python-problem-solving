from functools import reduce

def square_nums(x):
    return x*x

result  = square_nums(5)
print(result)

# lamda arguments : expresion

sum_value = lambda x : x**2
print(sum_value(6))

students = [('Rahim', 60), ('Karim', 7), ('Fahim',8)]
sorted_students = sorted(students, key=lambda x:x[1], reverse=True) #here x extracting each value from 1 index(6,7,8)
print(sorted_students)

nums=[1,2,30]
sum = reduce(lambda x, y: x + y, nums)
print(sum)
