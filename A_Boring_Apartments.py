t = int(input())
while t > 0:
    ba_num = input()
    prev = (int(ba_num[0]) - 1) * 10
    curr = (1 + len(ba_num))*len(ba_num)//2
    print(prev + curr)
    t -= 1