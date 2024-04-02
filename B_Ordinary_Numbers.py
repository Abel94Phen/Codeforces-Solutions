t = int(input())
for _ in range(t):
    number = int(input())
    array = [_ for _ in range(1, 10)]
    i = 0
    ordinary_numbers = 0
    while array[i%9] <= number:
        array[i%9] = array[i%9] * 10 + array[i%9]%10
        ordinary_numbers += 1
        i += 1
    print(ordinary_numbers)