def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

# print(merge_sort([3,2,1,5,4]))


def quick_sort(lst):
    return quick_sort_helper(lst, 0, len(lst) - 1)

def quick_sort_helper(lst, first, last):
    if first < last:
        split_point = partition(lst, first, last)
        quick_sort_helper(lst, first, split_point - 1)
        quick_sort_helper(lst, split_point + 1, last)

def partition(lst, first, last):
    pivot_value = lst[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and lst[left_mark] <= pivot_value:
            left_mark += 1
        while lst[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            temp = lst[left_mark]
            lst[left_mark] = lst[right_mark]
            lst[right_mark] = temp
    temp = lst[first]
    lst[first] = lst[right_mark]
    lst[right_mark] = temp
    return right_mark

# print(quick_sort([1,5,2,4,8]))

def radix_sort(lst):
    max_value = max(lst)
    exp = 1
    while max_value / exp > 0:
        counting_sort(lst, exp)
        exp *= 10
    return lst

def counting_sort(lst, exp):
    output = [0] * len(lst)
    count = [0] * 10
    for i in range(len(lst)):
        index = lst[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len(lst) - 1
    while i >= 0:
        index = lst[i] // exp
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(len(lst)):
        lst[i] = output[i]

# print(radix_sort([1,5,2,4,8]))

def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            temp = lst[j]
            lst[j] = lst[j - 1]
            lst[j - 1] = temp
            j -= 1
    return lst

# print(insertion_sort([1,5,2,4,8]))


def reverse_insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] > lst[j - 1]:
            temp = lst[j]
            lst[j] = lst[j - 1]
            lst[j - 1] = temp
            j -= 1
    return lst

# print(reverse_insertion_sort([1,5,2,4,8]))

