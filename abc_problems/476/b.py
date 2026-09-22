N = int(input())
S = input()
T = input()
ans = 'Yes'

for i in range(len(S)):
    if S[i]!=T[i] and T[i]!='*':
        ans = 'No'
        break

print(ans)