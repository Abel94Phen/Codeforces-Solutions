import sys, threading
input = lambda:sys.stdin.readline().strip()

def main():
    length, d = map(int, input().split())
    s = input()

    memo = [float('-inf') for _ in range(length)]
    def dp(index):
        if index == len(s) - 1:
            return 0

        if index >= len(s) or s[index] == '0':
            return float('inf')


        if s[index] == '1':
            if memo[index] == float('-inf'):
                memo[index] =  1 + min(dp(index + dx) for dx in range(1, d + 1))
        return memo[index]

    answer = dp(0)
    print(answer) if answer != float('inf') else print(-1)
    
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1<<27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

