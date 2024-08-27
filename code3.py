numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def number_of_occurrences(x):
    occurrences = 0
    first_index = None
    last_index = None
    for num in numbers :
        if num == x  :
            occurrences +=1
    return first_index , last_index , occurrences
x = 10
first_index, last_index, occurrences = number_of_occurrences(x)
print(f"First index: {first_index}, Last index: {last_index}, Occurrences: {occurrences}") 