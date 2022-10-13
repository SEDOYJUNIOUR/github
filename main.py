ls = [(1, 0), (2, 3), (3, -1), (4, 0), (3, 10)]
f = lambda x: bool(x[1])
a = sum(map(f, filter(f, ls)))
print(a)
print("Hello")
print("By")

