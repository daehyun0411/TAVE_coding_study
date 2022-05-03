N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0

def bomul(a,b):
    s = 0
    a.sort()
    for i in a:
        x = max(b)
        s += i * x
        b.pop(b.index(x))
    return print(s)

bomul(a,b)
