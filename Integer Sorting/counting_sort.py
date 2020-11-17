# Henry Calderon
# CS 2.1/Integer Sorting/counting_sort.py

'''
fundtion counting sort takes in list
    get the max value of the list
    create a new list of 0's that is the length of the max value + 1

    loop through original list:
        for each value, add + 1 to the value in the new list at the index that corresponds with the new value

    Loop
        Organize the values in the new array

    create an output array of the same length as the original array, none values as place holders

    Loop through new list? or loop through original:
        put values in output array based on index place and count of new array
'''

def counting_sort(list):
    # FIXME: Improve this to mutate input instead of creating new output list

    # TODO: Find range of given numbers (minimum and maximum integer values)
    max_val = max(list) + 1
    # Create new list of 0's
    # https://www.codegrepper.com/code-examples/python/create+a+list+of+a+certain+length+python

    # TODO: Create list of counts with a slot for each number in input range
    count_list = [0] * max_val

    # TODO: Loop over given numbers and increment each number's count
    # Loop through list and add count values
    for item in list:
        count_list[item] += 1

    number_of_items = 0
    for index, count in enumerate(count_list):
        count_list[index] = number_of_items
        number_of_items += count

    output_list = [None] * len(list)

    # TODO: Loop over counts and append that many numbers into output list
    for item in list:

        output_list[count_list[item]] = item
        count_list[item] += 1

    return output_list

print(counting_sort([0,10,6,5,20,1,13,1,5,8,16]))