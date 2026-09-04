N = int(input())
A = list(map(int, input().split()))
first = N//2
ans = 0

for i in range(first, N):
    ans += A[i]

print(ans)