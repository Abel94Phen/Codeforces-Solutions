import sys, threading
input = lambda: sys.stdin.readline().strip()

def main():
    n, x = map(int, input().split())
    distressed = 0
    for _ in range(n):
        sign, val = input().split()
        if sign == '+':
            x += int(val)
        else:
            if int(val) <= x:
                x -= int(val)
            else:
                distressed += 1
    print(x, distressed)

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

