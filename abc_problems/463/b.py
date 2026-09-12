N, X =input().split()
N = int(N)
S = [input() for _ in range(N)]
ans = 'No'

for i in range(N):
    match X:
        case 'A':
            if S[i][0] == 'o':
                ans = 'No'
                break
        case 'B':
            if S[i][1] == 'o':
                ans = 'No'
                break
        case 'C':
            if S[i][2] == 'o':
                ans = 'No'
                break
        case 'D':
            if S[i][3] == 'o':
                ans = 'No'
                break
        case 'E':
            if S[i][4] == 'o':
                ans = 'No'
                break
print(ans)