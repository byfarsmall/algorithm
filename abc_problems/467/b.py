N = int(input())
diff = 0

for _ in range(N):
    A, B, S = input().split()
    A, B = map(int, (A, B))

    if S=='keep':
        diff += B-A

print(diff)