def min_string_factor(X, Y, S, R):
    from collections import defaultdict

    n = len(X)
    dp = [(float('inf'), float('inf')) for _ in range(n+1)]
    dp[0] = (0, 0)  # (min_substrings, min_cost)

    # Build set of all substrings of Y and reversed Y
    substr_Y = set()
    substr_YR = set()
    len_Y = len(Y)
    Y_rev = Y[::-1]

    for i in range(len_Y):
        for j in range(i+1, len_Y+1):
            substr_Y.add(Y[i:j])
            substr_YR.add(Y_rev[i:j])

    # DP processing
    for i in range(1, n+1):
        for j in range(i):
            sub = X[j:i]
            if sub in substr_Y:
                new_count = dp[j][0] + 1
                new_cost = dp[j][1] + S
                if new_count < dp[i][0] or (new_count == dp[i][0] and new_cost < dp[i][1]):
                    dp[i] = (new_count, new_cost)
            if sub in substr_YR:
                new_count = dp[j][0] + 1
                new_cost = dp[j][1] + R
                if new_count < dp[i][0] or (new_count == dp[i][0] and new_cost < dp[i][1]):
                    dp[i] = (new_count, new_cost)

    if dp[n][0] == float('inf'):
        return "Impossible"
    else:
        return dp[n][1]


# -------------------------
# Input Reading
# -------------------------
if __name__ == "__main__":
    X = input().strip()
    Y = input().strip()
    S, R = map(int, input().strip().split())

    result = min_string_factor(X, Y, S, R)
    print(result)
