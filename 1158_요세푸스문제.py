N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]

ans = []
num = 0

for _ in range(N):
    num += K - 1
    if num >= len(arr):
        num = num % len(arr)

    ans.append(str(arr.pop(num)))
print("<", ", ".join(ans)[:], ">", sep='')