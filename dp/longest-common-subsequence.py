def LCS(x, y):
    m = len(y)
    n = len(x)
    LMatrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                LMatrix[i][j] = LMatrix[i-1][j-1] + 1
            else:
                LMatrix[i][j] = max(LMatrix[i-1][j], LMatrix[i][j-1])
    
    print(' the length of the length common subsequence is:', LMatrix[n][m])

    i, j = n, m
    subsequence = ""
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            subsequence = x[i-1] + subsequence
            i -= 1
            j -= 1
        elif LMatrix[i-1][j] > LMatrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    return subsequence
  
assert(LCS("AGGTAB", "GAXTXA") == "GTA")