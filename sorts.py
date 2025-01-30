def selection_sort(A):
    for i in range(0, len(A) - 1):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def bubble_sort(A):
    n = len(A)
    for a in range(1, n):
        for i in range(n - a):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]

def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

def quick_sort(A):
    if len(A) > 1:
    	pivot = A[len(A) // 2]
    	left = [x for x in A if x < pivot]
    	middle = [x for x in A if x == pivot]
    	right = [x for x in A if x > pivot]
    	return quick_sort(left) + middle + quick_sort(right)

def heapify(A, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and A[i] < A[left]:
        largest = left
    if right < n and A[largest] < A[right]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

def heap_sort(A):
    n = len(A)
    for i in range(n//2, -1, -1):
        heapify(A, n, i)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

def shell_sort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap //= 2
    return A

def shell_sort_hibbard(A):
    n = len(A)
    gap = 1
    gaps = []
    while gap < n:
        gaps.append(gap)
        gap = 2 * gap + 1

    for gap in reversed(gaps):
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
    return A

def shell_sort_pratt(A):
    n = len(A)
    gaps = []
    i = j = 1
    while 2**i - 1 < n or 3**j - 1 < n:
        if 2**i - 1 < n:
            gaps.append(2**i - 1)
            i += 1
        if 3**j - 1 < n:
            gaps.append(3**j - 1)
            j += 1

    gaps = sorted(set(gaps), reverse=True)

    for gap in gaps:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
    return A
