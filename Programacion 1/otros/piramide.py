n = int(input())
c = input()

for i in range(n):
    print(c*i, "        ", i)
for i in range(n, 0, -1):
    print(c*i, "        ", i)
