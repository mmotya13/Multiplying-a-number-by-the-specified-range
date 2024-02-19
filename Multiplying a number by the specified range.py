n1 = int(input('Your number is... '))
n2 = int(input('You will mutiply it to... '))
lst = []
for j in range(1, n2+1):
    lst.append(j)
for i in lst:
    print(f'{n1}x{i} =', n1*i)