S = input()

for i in range(len(S)):
    print(S[i],end='')
    if i != len(S)-1:
        print('o', end='')