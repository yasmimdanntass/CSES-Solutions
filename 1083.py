
a = int(input())
seq = []

for i in range(1, a+1):
    seq.append(i)

seq_user = sorted(list(map (int,(input().split()))))

for i in range(len(seq_user)):
    if seq_user[i] != seq[i]:
        print(seq[i])
        break
    
    elif i == len(seq_user) - 1:
        print(seq[i+1])
        break