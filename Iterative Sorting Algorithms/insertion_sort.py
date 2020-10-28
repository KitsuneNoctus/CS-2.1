#Henry Calderon CS 2.1

'''
for loop through items
    while its in range and the key item is less than the item before
        switch items
'''

def insertion_sort(items):

    for i in range(len(items)):
        main = items[i]
        k = i-1
        while k >= 0 and main < items[k]:
            items[k+1], items[k] = items[k], items[k+1]
            k -= 1


if __name__ == "__main__":
    nums = [12, 11, 13, 5, 6]
    insertion_sort(nums)
    print(nums)