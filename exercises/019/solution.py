import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
if len(sys.argv) > 2:
    print(x + y)
else:
    print("usage: python3 solution.py PARAM")

