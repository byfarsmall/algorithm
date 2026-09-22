N = int(input())
A = list(map(int, input().split()))
a = []

for i in range(3):
    a.append(A[i])

a.sort(reverse='True')
print(a[2])

for i in range(3, N):
    if a[2]<A[i]:
        a[2] = A[i]
        a.sort(reverse='True')
    print(a[2])

