N = int(input())
S = list(input())
ans = 0

for n in range(N): 
    if S[max(0, n-1)] == 'o':
        continue
    if S[n] == 'o':
        continue
    if S[min(N-1, n+1)] == 'o':
        continue
    ans += 1

print(ans)