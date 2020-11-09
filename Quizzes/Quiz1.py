# Henry Calderon
# Quizzes/Quiz1.py

def raise_power(number, power, result=None):
    # Iterative Case
    # mult = number
    # for i in range(1,power):
    #     mult = mult * number

    if result == None:
        result = number

    # base case
    if power == 0:
        return 1

    # Base Case #2
    if power == 1:
        result = number
        return result
    else:
        power = power - 1
        return raise_power(number, power, result) * result

print(raise_power(4,2))
print(raise_power(2,4))
print(raise_power(3,5))
print(raise_power(0,0))