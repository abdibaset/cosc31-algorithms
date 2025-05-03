def FindX(A,k, n, x):
    if A[1] < x:
        return FindXHelper(A[k+1:], k+1, n, x)
    else:
        return FindXHelper(A[:k], k, 0, x)
def FindXHelper(A, left, right, x):
    mid = (left + right) // 2
    print('left:', left, 'right:', right, 'mid:', mid, 'array:', A) 
    if A[mid] == x: return True
    if A[mid] < x: return FindXHelper(A[mid+1:], mid+1, right, x)
    else: return FindXHelper(A[:mid], left, mid, x)

assert FindX([5, 4, 3, 2, 1, 0, 6, 7, 8, 9, 10], 5, 10, 3) == False