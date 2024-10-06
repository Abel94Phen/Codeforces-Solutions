def validate(matrix):
    condition_1 = matrix[0][0] < matrix[0][1] and matrix[1][0] < matrix[1][1]
    condition_2 = matrix[0][0] < matrix[1][0] and matrix[0][1] < matrix[1][1]
    return condition_1 and condition_2

def rotate(matrix):
    matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1] = matrix[1][0], matrix[0][0], matrix[1][1], matrix[0][1]

t = int(input())
for _ in range(t):
    matrix = []
    for _ in range(2):
        matrix.append(list(map(int, input().split())))
    
    for i in range(4):
        if validate(matrix):
            print("YES")
            break
        rotate(matrix)
    else:
        print("NO")