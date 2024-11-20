t = int(input())
for _ in range(t):
    a = int(input())
    answer = 2**(a.bit_length()) - 1
    if answer == a:
        answer, d = 1, 2
        while d * d <= a:
            if a%d == 0:
                answer = max(d, a//d)
            d += 1
        print(answer)
    else:
        print(answer)