count = m = 0
f = open('17.txt')
a = [int(i) for i in f]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] - a[j]) % 2 == 0 and (a[i] % 31 == 0 or a[j] % 31 == 0):
            count += 1
            m = max(m, a[i] + a[j])
print(count, m)