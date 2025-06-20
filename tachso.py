import sys
sys.stdin = open("tachso.inp")
sys.stdout = open("tachso.out", "w")

n = int(input())
cnt = 0
for b in range(1, n-1):
    for c in range(1, n-1):
        a = n - b - c
        if a > 1 and b % a == 0 and c % a == 0:
            cnt += 1
print(cnt)


