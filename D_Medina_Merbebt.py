t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))

    ## Prefix Sum can't do this.