N = int(input())
P = list(map(int, input().split()))
ans = 'Yes'

for i in range(N):
    if ((i//10+1)*10)<P[i]:
        ans = 'No'
        break

print(ans)