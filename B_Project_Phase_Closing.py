from math import ceil

n, m, k = map(int, input().split())

lane = ceil(k/(2*m))
desk = ceil(((k - 1)%(2*m) + 1)/2)
posi = 'L' if k%2 else 'R'

print(lane, desk, posi)