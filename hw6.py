
d= 2
A = 0
B = 0
a = 2
b = 6

while A + B != 18 :
    print()
    if B == 9:
        a += 4
        b += 4
        B = 0
        print()
    B +=1
    for A in range(a, b):
        print(f'{A} x {B} = {A*B}', end=('  '))
