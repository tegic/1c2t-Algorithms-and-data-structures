from list_classes import List
from binary_search_tree import BinarySearchTree, TreeElement
from time import time_ns
from config import arrays, results
from create_avl import create_avl
import pprint
import math
import pandas as pd


# LIST
for i in range(len(arrays)):
    my_list = List()
    print(f'add_to_list {len(arrays[i])} elements')
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_list.add_sorted(arrays[i][j])
    results.append(['add_to_list_time', len(arrays[i]), round((time_ns() - s_time) * 10 ** -9, 5)])
    
    print(f'find_in_list {len(arrays[i])} elements')
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_list.find(arrays[i][j])
    results.append(['find_in_list_time', len(arrays[i]), round((time_ns() - s_time) * 10 ** -9, 3)])

    print(f'delete_in_list {len(arrays[i])} elements')
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_list.find(arrays[i][j])
    results.append(['delete_in_list_time', len(arrays[i]), round((time_ns() - s_time) * 10 ** -9, 3)])
    


# BST
for i in range(len(arrays)):
    my_BST = BinarySearchTree()
    print(f'add_to_BST {len(arrays[i])} elements')
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_BST.add(TreeElement(arrays[i][j]))
    results.append(['add_to_BST_time', len(arrays[i]), round((time_ns() - s_time) * 10 ** -9, 3)])
    
    print(f'find_in_BST {len(arrays[i])} elements')
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_BST.find(arrays[i][j])
    results.append(['find_in_BST_time', len(arrays[i]), round((time_ns() - s_time) * 10 ** -9, 3)])

    print(f'delete_in_BST {len(arrays[i])} elements')
    s_time = time_ns()
    for j in range(len(arrays[i]) - 1, 0, -1):
        my_BST.find(arrays[i][j])
    results.append(['delete_in_BST_time',  len(arrays[i]), round((time_ns() - s_time) * 10 ** -9, 3)])


# AVL
for i in range(len(arrays)):
    my_BST = BinarySearchTree()
    my_AVL = BinarySearchTree()
    print(f'add_to_BST {len(arrays[i])} elements')
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_BST.add(TreeElement(arrays[i][j]))
    results.append(['get_height_of_BST', len(arrays[i]), my_BST.find_height()])
    
    my_AVL.first_el = create_avl(my_BST.get_inorder())
    results.append(['get_height_of_AVL', len(arrays[i]), my_AVL.find_height()])
    

df1 = pd.DataFrame(results, columns=['Operation', 'Elements count', 'Value'])

with pd.ExcelWriter('Result.xlsx', engine='xlsxwriter') as writer:
    df1.to_excel(writer, sheet_name='Sheet 1', index=False)

    workbook = writer.book
    worksheet = writer.sheets['Sheet 1']

