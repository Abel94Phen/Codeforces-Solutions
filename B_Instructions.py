import sys, threading
input = lambda:sys.stdin.readline().strip()

def main():
    t = int(input())

    def calculate(index, array):
        if index >= length:
            return 0

        if memo[index] == -1:
            memo[index] = array[index] + calculate(index + array[index], array)
        return memo[index]

    for _ in range(t):
        length = int(input())
        array = list(map(int, input().split()))

        memo = [-1 for _ in range(length)]
        for i in range(length):
            if memo[i] == -1:
                calculate(i, array)
        print(max(memo))

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1<<27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




    

