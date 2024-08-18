s = input()
k = int(input())

if k > len(s):
    print("impossible")
else:
    unique_count = len(set(s))
    if unique_count >= k:
        print(0)
    else:
        print(k - unique_count)

