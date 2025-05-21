from array_with_unique_values import create_array_with_unique_values
from list_classes import List

min_value = 0
max_value = 100
count_of_values = 10 
array_list = create_array_with_unique_values(count_of_values, min_value, max_value)


my_list = List()
print(array_list)
for i in range(len(array_list)):
    my_list.add_sorted(array_list[i])

my_list.print()
