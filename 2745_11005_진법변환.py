# 문제
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.

# 진짜 간단하게 푼 방법
import sys

a, b = sys.stdin.readline().split()

print(int(a, int(b)))

# 원리 이해 풀이
# ex) ZZZZZ 36 => 35 * 36^4 + 35 * 36^3 + 35 * 36 ^2 + 35 * 36^1 + 35 * 36^0
N, B = input().split()
B = int(B)

answer = 0
for i, ch in enumerate(N[::-1]):  # i가 0부터 시작하기 때문에 뒤집어서 0제곱부터 처리
    if ch.isdigit():
        value = int(ch)
    else:
        value = ord(ch) - 55   # ASCII 코드 변환 후 A가 10이 되게 빼주기
    answer += value * (B ** i)

print(answer)

# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 10진법 수 N을 B진법으로 출력한다.

# 진수 b로 나눈 나머지값을 거꾸로 반환하면 b진법이 됨
import sys

n, b = map(int,sys.stdin.readline().split())

l = []
while n > 0:
    rem = n % b
    n = n // b
    
    if rem > 9:
        l.append(chr(rem + 55))
    else:
        l.append(str(rem))
        
print(''.join(reversed(l)))
