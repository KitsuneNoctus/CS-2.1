#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # FIXME: Improve this to mutate input instead of creating new output list

    # TODO: Find range of given numbers (minimum and maximum integer values)
    if numbers == []:
        return []
    max_val = max(numbers) + 1
    # Create new list of 0's
    # https://www.codegrepper.com/code-examples/python/create+a+list+of+a+certain+length+python

    # TODO: Create list of counts with a slot for each number in input range
    count_list = [0] * max_val

    # TODO: Loop over given numbers and increment each number's count
    # Loop through list and add count values
    for item in numbers:
        count_list[item] += 1

    number_of_items = 0
    for index, count in enumerate(count_list):
        count_list[index] = number_of_items
        number_of_items += count

    output_list = [None] * len(numbers)

    # TODO: Loop over counts and append that many numbers into output list
    for item in numbers:

        output_list[count_list[item]] = item
        count_list[item] += 1

    return output_list


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

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # FIXME: Improve this to mutate input instead of creating new output list

    if numbers == []:
        return []

    new_list = []
    # TODO: Find range of given numbers (minimum and maximum values)
    min = numbers[0]
    max = numbers[0]

    for item in numbers:
        if min > item:
            min = 1
        if max < item:
            max = item

    # TODO: Create list of buckets to store numbers in subranges of input range
    for i in range(0,len(numbers)):
        new_list.append([])

    # TODO: Loop over given numbers and place each item in appropriate bucket
    for item in numbers:
        unique_index = int(item * len(numbers) / (max + 1))
        new_list[unique_index].append(item)

    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    for i in range(len(new_list)):
        new_list[i] = bubble_sort(new_list[i])

    numbers.clear() #Empty the list

    # TODO: Loop over buckets and append each bucket's numbers into output list
    for i in range(len(new_list)):
        for item in new_list[i]:
            numbers.append(item)

    return numbers