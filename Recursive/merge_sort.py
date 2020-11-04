# Henry Calderon CS 2.1
# Recursive/merge_sort.py

'''
If the list is not a single item
    break the list in two down the middle
    do that again

    Then we need to put it back together
    While going through both lists
        check to see if 
'''


'''
https://medium.com/karuna-sehgal/a-simplified-explanation-of-merge-sort-77089fe03bb2
https://www.geeksforgeeks.org/merge-sort/

def merge_sort(array):
    THIS VERSION GETS AN ERROR
  #return a sorted array

  #base case
  if len(array) == 1: #a list of 1 is already sorted
    return array

  #recursive case
  middle = len(array) // 2
  #gimmie the left chunk and the right chunk
  left = array[0:middle + 1]
  right = array[middle + 1:]
  print(left)
  print(right)

  resultleft = merge_sort(left)
  resultright = merge_sort(right)
  return merge(resultleft, resultright)


def merge(left, right):
  #TODO: return a merged sorted version of left and right combined
  pass

merge_sort([8, 1, 9, 14, 23])

SOMETHING to Look Over
https://stackabuse.com/merge-sort-in-python/
'''

# MARK: DOESN'T WORK
def merge_sort(items):
    # print("Calling")
    # if len(items) > 1:
    #     mid = len(items)//2 + 1
    #     left = items[0:mid]
    #     right = items[mid:]
    #     print(left)
    #     print(right)

    #     return merge(merge_sort(left), merge_sort(right))
    # return items

    if len(items) <= 1:
        return items
    
    mid = len(items)//2
    left = items[0:mid]
    right = items[mid:]
    # print(left)
    # print(right)
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    print("---Merge---")
    print(f"Left: {left}")
    print(f"Right: {right}")
    merged = []
    l_index = r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            merged.append(left[l_index])
            l_index += 1
        else:
            merged.append(right[r_index])
            r_index += 1
    print(f"Merged: {merged}")
    print(f"left index {l_index} && right index {r_index}")
    # return result.concat(left.slice(indexLeft)).concat(right.slice(indexRight))
    merging = merged + left[l_index:] + right[r_index:]
    return merging


print("--------Sorting--------")
print(merge_sort([10,5,6,11,3,4,2]))
print("--------Sorting--------")
print(merge_sort([8, 1, 9, 14, 23]))

    