N  = int(input())
A = list(map(int, input().split()))
cnt = 0

while(len(A)==N):
    new_A = []
    for a in A:
        if a%2 == 1:
            print(cnt)
        else:
            new_A.append(a//2)
    cnt += 1
    A = new_A.copy()
    