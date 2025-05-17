# file = open('file.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# print('-------------------------')

with open('file.txt', 'r') as file:
    content = file.read()
    print(content)

# with open('file.txt', 'w') as f:
#     f.write('\n Hi, This is Ahmed')
#     f.write('\n Hi, This is Ahmed2')


with open('file.txt', 'a') as f:
    f.write('\n Hi, This is Ahmed \n')
    f.write('Hi, This is Ahmed2\n')

lines = ['\nI love python\n', "I'm learning python for 15days"]
with open('file.txt', 'a') as f:
    f.writelines(lines)
