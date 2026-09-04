N = int(input())
A = list(map(int, input().split()))
A.sort()
A_sum = sum(A)
i = 0
d_sum = 0

while(i<N-1):
    if A[i] == A[i+1]:
        d_sum += A[i]*2
        i += 2
    else:
        i += 1
print(A_sum - d_sum)