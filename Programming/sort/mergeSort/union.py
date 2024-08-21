def merge(A, B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)

    # while i+j < m+n :  # i+j is the number of elements merged so far
    #     if i == m:   # Case 1: A is empty
    #         C.append(B[j])
    #         j += 1
    #     elif j == n:   # Case 2: B is empty
    #         C.append(A[i])
    #         i += 1
    #     elif A[i] <= B[j]:   # Case 3: Head of A is smaller
    #         C.append(A[i])
    #         i += 1
    #     elif A[i] >= B[j]:   # Case 4: Head of B is smaller
    #         C.append(B[j])
    #         j += 1
    # return C

    while i < m and j < n:
        if A[i] < B[j]:
            if A[i] not in C:
                C.append(A[i])
            i += 1
        elif B[j] < A[i]:
            if B[j] not in C:
                C.append(B[j])
            j += 1
        else:  # if both equal, append A[i] and increment both i&j
            if A[i] not in C:
                C.append(A[i])
            i += 1
            j += 1

    while i < m:
        if A[i] not in C:
            C.append(A[i])
        i += 1

    while j < n:
        if B[j] not in C:
            C.append(B[j])
        j += 1

    return C


def MergeSort(A, left, right):
    if right - left <= 1:
        return A[left:right]

    mid = (left + right) // 2
    L = MergeSort(A, left, mid)
    R = MergeSort(A, mid, right)

    return merge(L, R)


def union(list1, list2):
    merged_list = list1 + list2
    sorted_list = MergeSort(merged_list, 0, len(merged_list))
    return sorted_list


# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(union(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]