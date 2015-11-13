t = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    for j in range(26):
        if t[i] != t[j]:
            print(t[i]+t[j])
