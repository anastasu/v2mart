f = open("24.txt")
s = f.read()
d = dict()
for i in range(len(s)-1):
    if s[i] == 'A' and s[i+1] != 'A':
        if s[i+1] not in d:
            d[s[i+1]] = 1
        else:
            d[s[i+1]] += 1
max_key = max(d, key=d.get)
print(max_key)