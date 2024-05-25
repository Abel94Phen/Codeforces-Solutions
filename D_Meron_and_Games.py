from collections import Counter
import sys, threading
input = lambda:sys.stdin.readline().strip()

def main():
    length = int(input())
    array = list(map(int, input().split()))

    hashcount = Counter(array)        
    for num in hashcount:
        hashcount[num] *= num
    
    array = list(hashcount.keys())

    def dp(index):
        if nums[index] in restricted:
            return 0
        
        restricted.add(nums[index] - 1)
        restricted.add(nums[index] + 1)

        return hashcount[nums[index]] 

    print(score)

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1<<27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

