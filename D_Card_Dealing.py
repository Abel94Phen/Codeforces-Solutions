t = int(input())

for _ in range(t):
    n = int(input())
    alice = 1
    bob = 0
    n -= 1
    turn = False
    i = 2
    while i <= n:
        if turn:
            for _ in range(2):
                if i <= n:
                    alice += i
                    n -= i
                    i += 1
                else:
                    alice += n
                    n = 0
                    
        else:
            for _ in range(2):
                if i <= n:
                    bob += i
                    n -= i
                    i += 1
                else:
                    bob += n
                    n = 0
        turn = not turn
    
    if n:
        if turn:
            alice += n
        else:
            bob += n
            
    print(alice, bob)