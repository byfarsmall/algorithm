N = int(input())

ans = [[] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    K = row[0]
    A = row[1:]

    for a in A:
        ans[a - 1].append(i + 1)

for i in range(N):
    print(len(ans[i]), end=" ")

    for person in ans[i]:
        print(person, end=" ")

    print()