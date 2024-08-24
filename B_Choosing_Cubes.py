t = int(input())

for _ in range(t):
    n, f, k = map(int, input().split())
    
    cubes = list(map(int, input().split()))
    
    favorite = cubes[f - 1]
    
    cubes.sort(reverse = True)
    
    
    if favorite < cubes[k - 1]:
        print("NO")
    else:
        if k != n and favorite == cubes[k - 1] == cubes[k]:
            print("MAYBE")
        else:
            print("YES")
    