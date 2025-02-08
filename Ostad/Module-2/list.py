a = [1,2,3,4,5,6]
# a_new = []
# for i in a:
#     a_new.append(i**2)
# print(a_new)
a_new = [i**2 for i in a]
print(a_new)
print('-------------------------------')

b_new = [i**2 for i in a if i % 2 ==0]
print(b_new)
print('-------------------------------')
c_new = ['Even' if i % 2 == 0 else 'Odd' for i in a ]
print(c_new)
