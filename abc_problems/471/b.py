N = int(input())
dic = {}

for _ in range(N):
    S = input().lower()
    if S not in dic:
        dic[S] = 1
    else:
        dic[S] += 1


print(max(dic.values()))