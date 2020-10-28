# Henry Calderon CS 2.1

'''
loop through values
assign first among unsorted as highest
    Check if next value is higher
        If it is, switch highest to that number
at end of loop, move highest value to end
start loop again, minus 1 in length
'''

def selection_sort(items, reduction=0):
    high_index = 0
    for i in range(len(items)-reduction):
        if items[high_index] < items[i]
            high_index = i

    items.append(items.pop(high_index))

    reduction = reduction + 1
    selection_sort(items, reduction)
    sorted = selection_sort(items, reduction)

    return sorted


print(selection_sort([]))
