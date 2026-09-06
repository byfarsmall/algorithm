N, Q = map(int, input().split())
P = list(map(int, input().split()))
used = [False]*(N+1)
moved = []
unique = []

for q in range(Q):
    a =int(input())
    moved.append(a)

for m in reversed(moved):
    if not used[m]:
        used[m] = True
        unique.append(m)

for p in P:
    if not used[p]:
        print(p, end=" ")

for u in reversed(unique):
    print(u, end=" ")