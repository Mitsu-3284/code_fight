#小銭の組み合わせ

N = int(input())
a = 0

if N % 100 != 0:
    print("-1")

else :
    a = a + (N // 500)
    a = a + (N % 500) //100
    print(a)