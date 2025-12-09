import sys

N = int(sys.stdin.readline())

i = 2
// 곱으로 이루어진 한 쌍 중에서 작은 수는 루트N 이하이기 때문에 제곱으로 조건
while i * i <= N:
    while N % i == 0:
        print(i)
        N //= i
    i += 1

if N > 1:
    print(N)
