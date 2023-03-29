def findLargestSquareSize(samples):
    n = len(samples)
    m = len(samples[0])

    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = samples[i][0]
    for j in range(m):
        dp[0][j] = samples[0][j]

    for i in range(1, n):
        for j in range(1, m):
            if samples[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    return max([max(row) for row in dp])