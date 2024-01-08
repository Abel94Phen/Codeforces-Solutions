def isPrime(number):
    for i in range(2, number):
        if not number%i:
            return False
    return True

number = int(input())

a = 4
b = number - a

while isPrime(a) or isPrime(b):
    a += 1
    b -= 1

print(a,b)