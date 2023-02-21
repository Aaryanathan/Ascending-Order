a = [90,27,3,45,92,1,76]
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            n = a[i]
            a[i] = a[j]
            a[j] = n
print(a)