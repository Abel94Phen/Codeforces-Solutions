n = int(input())
gens = list(map(int, input().split()))
gens.sort()

print(gens[n//2])