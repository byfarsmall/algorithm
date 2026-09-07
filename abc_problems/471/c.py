N = int(input())
A = list(map(int, input().split()))

A.append(0)
A.sort()

idx = A.index(0)
l = idx
r = idx

ans = 0
c = 0

for _ in range(N):
    if l - 1 >= 0:
        dl = abs(A[l - 1] - c)
    else:
        dl = float("inf")

    if r + 1 < len(A):
        dr = abs(A[r + 1] - c)
    else:
        dr = float("inf")

    if dl <= dr:
        ans += dl
        l -= 1
        c = A[l]
    else:
        ans += dr
        r += 1
        c = A[r]

print(ans)