s = input()
a = []
b = 0

for alpha in s:
    if alpha.isalpha():
        a.append(alpha)
    else:
        b += int(alpha)
        
        
a.sort()

if b != 0:
    a.append(str(b))

print(''.join(a))