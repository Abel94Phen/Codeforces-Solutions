n = int(input())
array = [0 for _ in range(n - (n%3))]
for i in range(0, n - (n%3), 3):
    print(f"? {i + 1} {i + 2}")
    ab = int(input())
    print(f"? {i + 2} {i + 3}")
    ba = int(input())
    print(f"? {i + 1} {i + 3}")
    ac = int(input())

    array[i] = ((ab + ba + ac) - 2*ba) // 2
    array[i + 1] = ((ab + ba + ac) - 2*ac) // 2
    array[i + 2] = ((ab + ba + ac) - 2*ab) // 2

index = 3 * (n//3)
for i in range(n%3):
    print(f"? {index} {index + 1}")
    total = int(input())
    array.append(total - array[-1])
    index += 1
print('!', *array)