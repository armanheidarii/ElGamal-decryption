p = 263
y_1 = 9
y_2 = 237
m = 131

for i in range(2, p):
    inv = -1
    for j in range(p):
        if ((y_1**i) * j) % p == 1:
            inv = j

    if (y_2 * inv) % p == m:
        print(f"d is {i} and ({y_1}^{i})^-1 = {inv}")
