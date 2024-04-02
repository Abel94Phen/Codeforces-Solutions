number, k = list(map(int, input().split()))
while k > 0:
    if number%10:
        number -= 1
    else:
        number //= 10
    k -= 1
print(number)