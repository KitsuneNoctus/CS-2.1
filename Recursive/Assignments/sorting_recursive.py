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
    TODO: Running time: O(n log(n)) It goes through the whole list only once, but piece by piece. 
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
    # print("Parting")
    pivot = items[low]
    start = low + 1
    end = high

    # TODO: Loop through all items in range [low...high]
    while True:
        # TODO: Move items less than pivot into front of range [low...p-1]
        while start <= end and items[end] >= pivot:
            end = end - 1
        # TODO: Move items greater than pivot into back of range [p+1...high]
        while start <= end and items[start] <= pivot:
            start = start + 1

        if start <= end:
            # print("Switch")
            items[start], items[end] = items[end], items[start]
        else:
            # print("Break")
            break
    # TODO: Move pivot item into final position [p] and return index p
    items[low], items[end] = items[end], items[low]
    return end


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n log(n)) under the circumstances that it's length is a less than 2 I would assume
    TODO: Worst case running time: O(n^2) it has to go through the whole list once, then each sub part of the 
    list broken down
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low == None and high == None:
        low = 0
        high = len(items)-1

    # TODO: Check if list or range is so small it's already sorted (base case)
    # if len(items) == 1:
    #     return items
    # print(low)
    # print(high)
    if low >= high:
        return


    # TODO: Partition items in-place around a pivot and get index of pivot
    part = partition(items, low, high)
    # TODO: Sort each sublist range by recursively calling quick sort
    quick_sort(items,low,part-1)
    quick_sort(items,part+1,high)

    return items