#DP+Memoisation appproach

def LCS(u,v):  #u[0 ... m-1], v[0 ... n-1]
    for r in range(len(u)+1):
        LCS[r][len(v)+1] = 0 #initialize rows with 0
    for c in range(len(v)+1):
        LCS[len(u)+1][c] = 0 #initialize cols with 0

    for c in range(len(v)+1, -1, -1):
        for r in range(len(u)+1, -1, -1):
            if u[r] == v[c]:
                LCS[r][c] = 1+LCS[r+1][c+1]
            else:
                LCS[r][c] = max(LCS[r+1][c], LCS[r][c+1])

    return(LCS[0][0]) # max value automatically propogates to 0,0 index

# Brute force : O(mn^2)
# DP : O(mn)
# DP+Memoisation : O(mn)