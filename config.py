from array_with_unique_values import create_array_with_unique_values

results = {
    'delete_in_list': {},
    'find_in_list': {},
    'add_to_list': {},
    'add_to_BST': {},
    'delete_in_BST': {},
    'find_in_BST': {},
    'get_height_of_AVL': {},
    'get_height_of_BST': {},
}
min_value = 0
max_value = 10000
round_numbers_count = 7
arrays = []
for i in range(200, 10001, 200):
    arrays.append(create_array_with_unique_values(i, min_value, max_value))
    print(f'created array with {i} elements')
