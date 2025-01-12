Red, Blue = map(int, input().split())
maximum, minimum = max(Red, Blue), min(Red, Blue)
petya, vesya = minimum - 1, minimum
petya += maximum - minimum
print(petya, vesya)