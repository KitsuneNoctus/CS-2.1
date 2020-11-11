# Henry Calderon
# Recursive/quicksort.py

'''
Function takes in items
    get mid point of items - set as pivot point
    get furthest left index and right index
    check to see if left is greater and right is smaller then pivot
        if one is, leave it and move the other approptiatley
        if it is, then switch the two items
        if they arent, move the pivots over

    once the indexs are right next to each other, split array into two groups based in pivot
        call quicksort on the two new lists (or do we want to not split two lists but just partition list)

'''

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    print("Parting")
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
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
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
    


array = [1,89,10,5,66,2]
print(f"Array is {array}")
print(f"Sorted: {quick_sort(array)}")