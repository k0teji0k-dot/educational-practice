N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    for heads in range(1, min(7, i) + 1):
        dp[i] = max(dp[i], dp[i - heads] * heads)
print(dp[N])