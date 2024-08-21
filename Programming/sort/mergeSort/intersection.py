def merge(A, B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)

    while i < m and j < n:
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        else:  # if both equal, append A[i] and increment both i&j
            if A[i] not in C:
                C.append(A[i])
            i += 1
            j += 1

    while i < m:
        i += 1

    while j < n:
        j += 1

    return C



def MergeSort(A, left, right):
    if right - left <= 1:
        return A[left:right]

    mid = (left + right) // 2
    L = MergeSort(A, left, mid)
    R = MergeSort(A, mid, right)

    return merge(L, R)


def intersection(list1, list2):
    sorted_list1 = MergeSort(list1, 0, len(list1))
    sorted_list2 = MergeSort(list2, 0, len(list2))
    return merge(sorted_list1, sorted_list2)


# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(intersection(list1, list2))  # Output: [4, 5]