N = int(input())
A = list(map(int, input().split()))
hyakuen_c = 0
jyuuen_c = 0
ichien_c = 0

for i in range(N):
    t = A[i]//1000 + 1 if A[i]%1000!=0 else A[i]//1000
    change = str(t*1000 - A[i]).zfill(3)
    hyakuen_c += int(change[0]) 
    jyuuen_c += int(change[1])
    ichien_c += int(change[2])

print(ichien_c, jyuuen_c, hyakuen_c, end=' ')
 