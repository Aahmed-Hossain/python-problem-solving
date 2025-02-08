a = {'Rahim': 21, 'Karim':55, 'Rejaul':24}
a['Karim'] = 88
a['Aminul'] = 99 # if not have in the dictionary that will be added if it had, it will be updated
print(a)

print(a.keys())
print(a.values())

for i in a.keys():
    print(i)
print('-----------------------------')

for k,v in a.items():
    # print(k,v)
    print(f'{k}:{v}')

# Get function
print('----------------------------')
print(a.get('hamim'))

# Dictionary comprehesion
a = { i: 'Even' if i % 2 == 0 else 'Odd' for i in range(1,16)}

print('----------------------------')
print(a)
