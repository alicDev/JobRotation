n = int(input())

a, b = 0, 1

while a < n:
    a, b = b, a + b

if a == n:
    print("pertence a sequência")
else:
    print("não pertence a sequência")