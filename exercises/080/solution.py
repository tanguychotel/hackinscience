t = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    for j in range(i, 26):
        if t[i] != t[j]:
            print(t[i]+t[j])
