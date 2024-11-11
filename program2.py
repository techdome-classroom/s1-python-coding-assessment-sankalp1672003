def decode_message( s: str, p: str) -> bool:

# write your code here

    m,n= len(s),len(p)
    decoder= [[False] * (n + 1) for _ in range(m + 1)]
    decoder[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            decoder[0][j] = decoder[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                decoder[i][j] = decoder[i][j - 1] or decoder[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                decoder[i][j] = decoder[i - 1][j - 1]

    return decoder[m][n]
