#決議

N, G, A = list(map(int,input().split()))
M = A // ((N + 1) // 2)
m = G - (N * G - A) // ((N + 1) // 2)

if M >= G :
    M = G

if m <= 0 :
    m = 0
    
print(M, m)
