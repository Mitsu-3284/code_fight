#アルファベットの横並べ



N = int(input())
C = [""] * N

for x in range(N):
    C[x] = input()

s = ""
for y in C:
    s = s + y
print(s,end="")
