from collections import Counter

N = int(input())
C = list(map(int,input().split()))

count = Counter(C)

print(N - max(count.values()))