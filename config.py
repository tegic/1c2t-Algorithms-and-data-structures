from array_with_unique_values import create_array_with_unique_values

min_value = 0
max_value = 10000
arrays = []
for i in range(1000, 10001, 1000):
    arrays.append(create_array_with_unique_values(i, min_value, max_value))