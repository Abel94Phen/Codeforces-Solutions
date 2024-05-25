t = int(input())


for _ in range(t):
    nodes = int(input())

    tree = {}
    moves = input()

    for i in range(1, nodes + 1):

        left, right = map(int, input().split())
        tree[i] = []

        if left == 0:
            tree[i].append(None)
        else:
            tree[i].append(left)

        if right == 0:
            tree[i].append(None)
        else:
            tree[i].append(right)

    

    
    

