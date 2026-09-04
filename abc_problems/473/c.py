from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
A_cnt = Counter(A)
C = sorted([A_cnt[i] for i in range(1, K+1)], reverse=True)

ans = 1

for i in range(1, K):
    if C[0] - C[i] > 1:
        break
    ans += 1
    
print(ans)