#!/usr/bin/python3 


def getMinMoves(s):
    n = len(s)
    inf = 10000000000

    dp_good = [[inf for j in range(26)] for i in range(n)]
    dp_bad = [[inf for j in range(26)] for i in range(n)]
    for c in range(26):
        dp_bad[0][c] = abs(ord(s[0]) - ord("a") - c)
    for i in range(1, n):
        prev_best = inf
        for c in range(26):
            prev_best = min(prev_best, dp_good[i - 1][c])
        for c in range(26):
            dp_good[i][c] = min(dp_bad[i - 1][c], dp_good[i - 1][c])
            dp_good[i][c] += abs((ord(s[i]) - ord("a")) - c)
            dp_bad[i][c] = prev_best + abs(ord(s[i]) - ord("a") - c)
    ans = inf
    for i in range(26):
        ans = min(ans, dp_good[n - 1][i])
    return ans


print(getMinMoves("acba"))