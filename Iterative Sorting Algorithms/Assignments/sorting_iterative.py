def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: Best and Worst time is O(n) as it will have to traverse the entire list
    to make sure that it is in order. It will only ever have to do it once.
    TODO: Memory usage: O(n) Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) Under the worst conditions of having to go through multiple times
    the case is as it is. It will continue to go through the list over and over until there isn't a swap
    during one of its runs.
    TODO: Memory usage: O(1) Why and under what conditions?"""

    swap = False
    # TODO: Repeat until all items are in sorted order
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            # TODO: Swap adjacent items that are out of order
            items[i], items[i+1] = items[i+1], items[i]
            swap = True

    if swap == True:
        items = bubble_sort(items)

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) It will always have to double loop through all items.
    TODO: Memory usage: O(1) Why and under what conditions?"""
    # Had to look up how to do this one, will explain how it works in video
    # TODO: Repeat until all items are in sorted order
    for i in range(len(items)):
        # TODO: Find minimum item in unsorted items
        min_in = i
        for j in range(i+1, len(items)):
            if items[min_in] > items[j]:
                min_in = j
        # TODO: Swap it with first unsorted item
        items[i],items[min_in] = items[min_in],items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n) is under the best conditions in that only one or no items need be switched.
    worst case is O(n^2) as it would be forced to 
    TODO: Memory usage: O(1) It takes up little space and thats under the worst conditions"""
    # TODO: Repeat until all items are in sorted order
    for i in range(len(items)):
        # TODO: Take first unsorted item
        main = items[i]
        k = i-1
        while k >= 0 and main < items[k]:
            # TODO: Insert it in sorted order in front of items
            items[k+1], items[k] = items[k], items[k+1]
            k -= 1