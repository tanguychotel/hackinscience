import sys


L=[]
for i in range(len(sys.argv)):
    L.append(sys.argv[i])
for v in enumerate(L):
    print(v)
