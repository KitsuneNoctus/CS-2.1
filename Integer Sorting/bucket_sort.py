# Henry Calderon
# Integer Sorting/bucket_sort.py

'''
Function takes in list:
    create a new list, empty
    for loop to create empty lists in empty list, to the same size of the list taken in
        new list append list

    for loop through original list
        use item and some kind of equation to get index
        append to the list at the index

    for loop though the linked list:
        sort each individual list

    for loop through indexs of linked list
        loop through each list in the bucket
            add the items back to the original list

    return the list, now in order
'''

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

def bucket_sort(list):
    # TODO: Find range of given numbers (min and max values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place them in the appropriate bucket
    # TODO: Sort Each bucket using any sorting algorithm (iterative or recursive)
    # TODO: Loop over buckets and append each buckets numbers into the output list
    # Stretch: Improve this to mutate input instead of creating a new output list
    new_list = []
    min = list[0]
    max = list[0]
    # Is max value the total of all items in the array?
    # Prior knowledge about values in your array
    #
    # Can be anything as long as max value fits numbers in your array
    # Is min value always 0?

    for item in list:
        if min > item:
            min = 1
        if max < item:
            max = item

    for i in range(0,len(list)):
        new_list.append([])

    for item in list:
        unique_index = int(item * len(list) / (max + 1))
        new_list[unique_index].append(item)

    for i in range(len(new_list)):
        new_list[i] = bubble_sort(new_list[i])

    list.clear() #Empty the list

    for i in range(len(new_list)):
        for item in new_list[i]:
            list.append(item)

    return list

print(bucket_sort([10,3,9,8,2,1,6,5,4,7]))