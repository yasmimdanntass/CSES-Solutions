sequence = input()

max_length = 0
count = 1

for i in range(1, len(sequence)):
    if sequence[i] == sequence[i - 1]:
        count += 1
    else:
        if count > max_length:
            max_length = count
        count = 1

max_length = max(max_length, count)

print(max_length)