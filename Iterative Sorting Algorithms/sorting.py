# Henry Calderon CS 2.1

def is_sorted(items):
    #TODO: return a bool indicating whether the items are sorted or not
    sorted = True
    for i in range(len(items)-1):
        if i+1 <= len(items):
            print("something")
            if items[i] > items[i+1]:
                sorted = False
    return sorted


    # This works just as well, looks better than what I have as well
    # for i in range(len(items)-1):
    #     if items[i] < items[i+1]:
    #         pass
    #     else:
    #         return False

print(is_sorted([1,3,5,10,20]))#expecting True
print(is_sorted([20,3,5,10,1]))#expecting False