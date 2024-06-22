n = 13**100
for i in range(1, n):
    x = {}
    for j in range(1, n):
        x[j] = False

    for j in range(1, n):
        x[(2**j) % n] = True

    flag = True
    for j in x:
        if x[j] == False:
            flag = False

    if flag:
        print(i)
