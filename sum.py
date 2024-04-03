n = int(input())
flag = False

for _ in range(n):
    a, b, c = map(int, input().split())

    if a + b == c or a + c == b or b + c == a:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")