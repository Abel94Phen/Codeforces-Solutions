from collections import defaultdict
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    coffees = list(map(int, input().split()))

    memo = defaultdict(int)

    def dp(index, cups, total):
        if total < 0:
            return float('inf')
        
        if index == len(coffees):
            return cups
        
        if index not in memo:
            
                drink = dp(index + 1, total + coffees[index])
            no_drink = dp(index + 1, total)
            memo[index] = max(drink, no_drink)

        return memo[index]
    
    print(dp(0, 0))
    # print(memo)   
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()