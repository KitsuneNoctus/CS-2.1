#!python


def merge(left, right):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    merged = []
    l_index = r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            merged.append(left[l_index])
            l_index += 1
        else:
            merged.append(right[r_index])
            r_index += 1
    merging = merged + left[l_index:] + right[r_index:]
    return merging

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    if len(items) <= 1:
        return items
    
    mid = len(items)//2
    left = items[0:mid]
    right = items[mid:]
    return merge(merge_sort(left), merge_sort(right))


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    pivot = len(items) // 2
    # TODO: Loop through all items in range [low...high]
    for i in range(low,high):
        # TODO: Move items less than pivot into front of range [low...p-1]
        if items[i] < items[pivot]:
            print("less")
        # TODO: Move items greater than pivot into back of range [p+1...high]
        if items[i] > items[pivot]:
            print("more")
    # TODO: Move pivot item into final position [p] and return index p
    return pivot #(????)


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low == None and high == None:
        low = 0
        high = len(items)-1
    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) == 1:
        return items
    # TODO: Partition items in-place around a pivot and get index of pivot
    part = partition(items, low, high)
    # TODO: Sort each sublist range by recursively calling quick sort
    quick_sort(items,low,part)
    quick_sort(items,part,high)

    return items