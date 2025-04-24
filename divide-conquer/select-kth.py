def FindPivot(arr):
    '''Find the median of medians of sub-arrays of size at most 5'''
    sub_arr_medians = []
    n = len(arr)
    ptr = 0

    while ptr  < n:
        if (n - ptr) < 5:
            sorted_sub_arr = sorted(arr[ptr: len(arr)])
        else:
            sorted_sub_arr = sorted(arr[ptr: ptr+5])
        sub_arr_medians.append(sorted_sub_arr[len(sorted_sub_arr)//2])
        ptr += 5
    if len(sub_arr_medians) == 1:
        return sub_arr_medians[0]
    return Select(sub_arr_medians, k = (len(sub_arr_medians) + 1) // 2)

def Partition(arr, _pivot):
    '''Quick sort, find left and right array of the pivot, and rank of pivot'''
    left_arr = [x for x in arr if x < _pivot]
    right_arr = [x for x in arr if x > _pivot]    
    pivot_index = len(left_arr) + 1

    return left_arr, right_arr, pivot_index

def Select(arr, k):

    if k < 1 or k > len(arr): return None
    if len(arr) == 1: return arr[0]

    # Find the pivot
    _pivot = FindPivot(arr)
    left, right, _rank = Partition(arr, _pivot)

    # recusive cases 
    if k == _rank: return _pivot
    elif k < _rank: return Select(left, k)
    else: return Select(right, k - _rank)

# Test cases
## edge cases
assert(Select([3, 2, 1, 4, 0, 5, 6, 7], 0) == None)
assert(Select([3, 2, 1, 4, 0, 5, 6, 7], 10) == None)
assert(Select([], 10) == None)

## normal cases
assert(Select([109], 1) == 109)
assert(Select([3, 2, 1, 4, 0, 5, 6, 7], 5) == 4)
assert(Select([3, 2, 1, 4, 0, 5, 6, 7], 1) == 0)
assert(Select([-3, 2, 1, -4, 0, 5, 6, 7], 2) == -3)
assert(Select([x for x in range(1001)], 99) == 98)

