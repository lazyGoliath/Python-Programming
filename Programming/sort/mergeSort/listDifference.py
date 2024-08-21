def merge(A,B):
    (C, m,n) = ([], len(A), len(B))
    (i,j) = (0,0)

    while i+j < m+n :
        if i == m:
            C.append(B[j])
            j += 1
        elif j == n:
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1