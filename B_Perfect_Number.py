k = int(input())

def digits_sum(number):
    total = 0
    while number:
        total += number%10
        number //= 10
    return total

perfect = 19

while k - 1:
    perfect += 9
    if digits_sum(perfect) == 10:
        k -= 1

print(perfect)