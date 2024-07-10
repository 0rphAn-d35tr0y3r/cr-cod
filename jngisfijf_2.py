numbers_list = [1, -2, 3, -4, -5, 6, -7, -8]

def remove_negatives(numbers):
    for number in numbers[:]:
        if number < 0:
            numbers_list.remove(number) 
    return numbers_list

print(remove_negatives(numbers_list))
 # Expected:[1, 3, 6]