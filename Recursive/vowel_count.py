'''Write a recursive function called vowel_count() to count the number of vowels in a given string, for example:
If you give vowel_count() the string “makeschool” it will return 4
'''

def vowel_count(word, index=0):
    # vowels = ["a","e","i","o","u"]
    count = 0

    if index > len(word)-1:
        return 0

    if word[index] == "a" or word[index] == "e" or word[index] == "i" or word[index] == "o" or word[index] == "u":
        count += 1

    #This works
    # if word[index] in vowels:
    #     count += 1
    index += 1

    return count + vowel_count(word, index)

print(vowel_count("makeschool"))#should print 4
print(vowel_count("dsfgh"))#should print 0


# AN EXAMPLE FROM ONLINE
# def isVowel(character): # function to check whether input character is a vowel
#   character = character.lower() # convert character to lower case so upper cases can also be handled
#   vowels = "aeiou" # string containing all vowels

#   if character in vowels: # check if given character is in vowels
#     return 1
#   else:
#       return 0

# def countVowels(string): # function that returns the count of vowels
# 	count = 0
# 	for i in range(len(string)): 
# 		if isVowel(string[i]) : # check if character is vowel 
# 			count += 1
# 	return count 

# # Driver code 
# string = "Educative"
# print(countVowels(string))