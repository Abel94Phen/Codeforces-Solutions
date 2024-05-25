from collections import defaultdict

import sys, threading
input = lambda:sys.stdin.readline().strip()

def main():
    n, a, b, c = map(int, input().split())

    memo = defaultdict(int)

    def calculate(n):
        if n == 0:
            return 0
        if n < 0:
            return -float("inf")

        if n not in memo:
            by_a = 1 + calculate(n - a)
            by_b = 1 + calculate(n - b)
            by_c = 1 + calculate(n - c)
            memo[n] = max(by_a, by_b, by_c)

            
        return memo[n]
    
    calculate(n)
    print(max(memo.values()))

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1<<27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




    









