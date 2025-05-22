from list_classes import List
from binary_search_tree import BinarySearchTree, TreeElement
from time import time_ns
from config import arrays
from create_avl import create_avl

"""
DONE!!!!!!!!!!!!
БАМБАЙЛЕЙЛА)))))))))))
"""

my_list = List()
my_BST = BinarySearchTree()

for i in range(len(arrays[0])):
    my_BST.add(TreeElement(arrays[0][i]))
    # for i in range(len(array)):
    #     my_list.add_sorted(array[i])
    #     my_BST.add(TreeElement(array[i]))

print(f"HEIGHT {my_BST.find_height()} for {len(arrays[0])} elements")
my_AVL = BinarySearchTree()
my_AVL.add(create_avl(my_BST.get_inorder()))
print(f"AVL HEIGHT {my_AVL.find_height()} for {len(arrays[0])} elements")

# my_BST.print()

# for i in range(len(array) - 1, 0, -1):
#     print(f"deleting {array[i]}")
#     my_BST.delete(array[i])
#     my_BST.print()

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