#TODO: write a recursive version of ispalindrome

def ispalindrome(my_string, li=None, ri=None):

  if li == None and ri == None:
    li=0
    ri = len(my_string)-1

  if li == ri:
    return True
  elif my_string[li] != my_string[ri]:
    return False
  elif li < ri:
    li += 1
    ri -= 1
    return ispalindrome(my_string, li,ri)

  return True

print(ispalindrome("tacocat")) #should print True
print(ispalindrome("tacoocat"))
print(ispalindrome("hello"))#should print False

# ALSO WORKS
# def is_palindrome(word):    
#     if len(word) < 2: 
#         return True
#     if word[0] != word[-1]: 
#         return False
#     return ispalindrome(word[1:-1])