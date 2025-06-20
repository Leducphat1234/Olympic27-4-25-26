import sys
sys.stdin = open("tachtonglientiep.inp")
sys.stdout = open("tachtonglientiep.out", "w")
from math import sqrt
n = int(input())
# n = (2a+k-1)*k/2
# k^2 + (2a-1)k - 2n = 0
# k = (-1 + √(2a-1)^2+8n)/2
cnt = 0
for a in range(1, n):
    k = (-(2*a-1) + sqrt((2*a-1)*(2*a-1)+8*n))/2
    if k < 0:
        k = (-(2*a-1) - sqrt((2*a-1)*(2*a-1)+8*n))/2
    if k - int(k) < 1e-7:
        print(a, k)
        cnt += 1
print(cnt)