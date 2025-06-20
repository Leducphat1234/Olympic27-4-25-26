import sys
sys.stdin = open("tongchuso.inp")
sys.stdout = open("tongchuso.out", "w")

n = int(input())
s = ""
while n > 0:
    if n >= 9:
        s += "9"
        n -= 9
    else:
        s += str(n)
        n = 0
print(s[::-1])