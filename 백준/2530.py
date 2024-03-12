A, B, C = map(int, input().split())

D = int(input())

M = D // 60
S = D % 60
H = M // 60
M %= 60

A += H
B += M
C += S

if C >= 60:
    B += C // 60
    C %= 60

if B >= 60:
    A += B // 60
    B %= 60

if A >= 24:
    A %= 24

print(A, B, C)