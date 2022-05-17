n = input()
length = len(n)
right = 0
left = 0

for i in range(length//2):
    right += int(n[i])
    
for j in range(length//2, length):
    left += int(n[j])
    
if right == left:
    print("LUCKY")
else:
    print("READY")
    