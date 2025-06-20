import sys
sys.stdin = open("daytongdoixung.inp")
sys.stdout = open("daytongdoixung.out", "w")

n = int(input())
a = [0]
for _ in range(n):
    a.append(int(input()))
pfsum = [0]
for i in range(1, n + 1):
    pfsum.append(pfsum[i-1] + a[i])
    
def binsearch(a, b) -> bool:
    left = a
    right = b
    while left <= right:
        mid = (left + right) // 2
        if pfsum[mid] - pfsum[a-1] == pfsum[b] - pfsum[mid]:
            return True
        elif pfsum[mid] - pfsum[a-1] < pfsum[b] - pfsum[mid]:
            left = mid + 1
        else:
            right = mid - 1
m = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        if binsearch(i, j):
            m = max(m, j - i + 1)
print(m)
