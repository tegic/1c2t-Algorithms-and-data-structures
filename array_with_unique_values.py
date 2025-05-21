from random import randint

def create_array_with_unique_values(count_of_values, min_number=0, max_number=False):
    """
    Function for creating array with unique values
    count_of_values - int (count_of_values >= 0)
    """
    if max_number == False or count_of_values > max_number - min_number:
        min_number = 0
        max_number = count_of_values
    count_of_values = int(count_of_values)
    if count_of_values < 0 or count_of_values > max_number - min_number:
        return False
    
    numbers_array = []
    i = 0

    while i < count_of_values:
        random_int = randint(min_number, max_number)
        if random_int in numbers_array:
            continue
        else:
            i += 1
            numbers_array.append(random_int)
    return numbers_array

if __name__ == "__main__":
    print(create_array_with_unique_values(7))
