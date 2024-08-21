# merging two lists

# O(n)
def merge(A,B):  # merge A[0:m] and B[0:n]
    (C, m, n) = ([], len(A), len(B))
    (i,j) = (0,0)  # current positions in A and B

    while i+j < m+n :  # i+j is the number of elements merged so far
        if i == m:   # Case 1: A is empty
            C.append(B[j])
            j += 1
        elif j == n:   # Case 2: B is empty
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:   # Case 3: Head of A is smaller
            C.append(A[i])
            i += 1
        elif A[i] >= B[j]:   # Case 4: Head of B is smaller
            C.append(B[j])
            j += 1
    return C

# O(log(n))
def MergeSort(A, left, right):
    # sort the slice A[left:right]

    if right - left <= 1:  # base case only 1/0 indices left in list
        return(A[left:right])
    
    (L,R) = ([],[])
    if right - left > 1:
        mid = (left+right)//2
        
        L = MergeSort(A, left, mid)
        R = MergeSort(A, mid, right)

    return merge(L,R)


list = [4,2,6,8,3,1,5,7]

print(MergeSort(list, 0, len(list)))