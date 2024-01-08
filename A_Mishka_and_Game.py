rounds = int(input())
Mishka, Chris = 0, 0
while rounds > 0:
    results = list(map(int, input().split()))
    if results[0] > results[1]:
        Mishka += 1
    elif results[0] < results[1]:
        Chris += 1
    rounds -= 1
    
if Mishka == Chris:
    print("Friendship is magic!^^")
elif Mishka < Chris:
    print("Chris")
else:
    print("Mishka")