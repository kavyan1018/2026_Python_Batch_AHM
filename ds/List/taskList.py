a = [2, 4, 6, 8, 10]
target = 12

for i in range(len(a)):
    for j in range(i + 1, len(a)):   # we dont need (2, 2)
        if a[i] + a[j] == target:
                print(f"Pair found: {a[i]} + {a[j]} = {target}")