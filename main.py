from array_with_unique_values import create_array_with_unique_values
from list_classes import List
from binary_search_tree import BinarySearchTree, TreeElement
from time import time_ns

min_value = 0
max_value = 100
count_of_values = 6
array = create_array_with_unique_values(count_of_values, min_value, max_value)

my_list = List()
my_BST = BinarySearchTree()

for i in range(len(array)):
    my_list.add_sorted(array[i])
    my_BST.add(TreeElement(array[i]))

my_BST.print()

for i in range(len(array) - 1, 0, -1):
    print(f"deleting {array[i]}")
    my_BST.delete(array[i])
    my_BST.print()

# cl = 0
# ct = 0

# start_cl = time_ns()
# for i in range(len(array)):
#     if my_BST.find(array[i]) != False:
#         ct += 1
# print(f"ct: {ct} {(time_ns() - start_cl) * 10 ** -9}s")

# start_ct = time_ns()
# for i in range(len(array)):
#     cl += my_list.find(array[i])
# print(f"cl: {cl} {(time_ns() - start_ct) * 10 ** -9}s")


# my_list.print()
# my_BST.print()