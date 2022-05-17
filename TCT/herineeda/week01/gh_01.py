number = list(map(int, input())) #입력값
length = len(number)//2 #길이의 절반
sum1 = sum(number[0:length])
sum2 = sum(number[length:])

if sum1 == sum2:
    print("LUCKY")
else: 
    print("READY")
