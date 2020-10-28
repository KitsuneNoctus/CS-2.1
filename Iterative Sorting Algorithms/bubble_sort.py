# Henry Calderon CS 2.1
# Bubble Sort

# loop through elements
#  check if current element is greater than next element
    # if it is, swap positions
    
# After it has looped, if a swap has ocurred, go again

def bubble_sort(items):
    '''O(n^2) time complexity'''
    swap = False
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            items[i], items[i+1] = items[i+1], items[i]
            swap = True

    if swap == True:
        items = bubble_sort(items)

    return items

print(bubble_sort([1,2,5,4,8,3]))