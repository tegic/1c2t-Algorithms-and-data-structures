from array_with_unique_values import create_array_with_unique_values
from list_classes import List

min_value = 0
max_value = 100
count_of_values = 10 
array = create_array_with_unique_values(count_of_values, min_value, max_value)

my_list = List()
my_list.print()

for i in range(len(array)):
    max_element_id = 0
    new_el_value = array[max_element_id]
    for j in range(len(array)):
        if array[j] > array[max_element_id]:
            max_element_id = j
            new_el_value = array[max_element_id]
    del array[max_element_id]
    my_list.add(new_el_value)

my_list.print()
