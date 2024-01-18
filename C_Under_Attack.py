t = int(input())
while t > 0:
    rows, cols = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    main_diagonal = {}
    second_diagonal = {}
    
    for i in range(rows):
        for j in range(cols):
            if i-j in main_diagonal:
                main_diagonal[i-j] += matrix[i][j]
            else:
                main_diagonal[i-j] = matrix[i][j]
    
    for i in range(rows):
        for j in range(cols):
            if i+j in second_diagonal:
                second_diagonal[i+j] += matrix[i][j]
            else:
                second_diagonal[i+j] = matrix[i][j]
    
    ans = 0

    for r in range(rows):
        for c in range(cols):
            cur_total =  main_diagonal[r - c] + second_diagonal[r + c] - matrix[r][c]
            ans = max(ans,cur_total)

    print(ans)
    t -= 1