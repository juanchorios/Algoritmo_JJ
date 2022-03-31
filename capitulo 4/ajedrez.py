str1='abc'
str2='123'

for char1 in str1:
    for char2 in str2:
        print(f'{char1}{char2}', end=' ')
X = 7
Y = 8
caballo_x = 0
caballo_y = 0
print(f'({caballo_x}, {caballo_y})', end=' ')
flow = True
while caballo_x != X and caballo_y != Y:
    if flow:
        caballo_x += 1
        caballo_y += 2
    else:
        caballo_x += 2
        caballo_y += 1
    print(f'({caballo_x}, {caballo_y})', end=' ')
    flow = not flow