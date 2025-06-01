from list_classes import List
from binary_search_tree import BinarySearchTree, TreeElement
from time import time_ns
from config import arrays, results, round_numbers_count
from create_avl import create_avl
import pprint
import math
import pandas as pd

def add_time_to_result_array(key_v, start_time, array=results):
    stop_time = round((time_ns() - start_time) * 10 ** -9, round_numbers_count)
    if stop_time == 0:
        if len(list(array[key_v].keys())) == 0:
            stop_time == 0
        else:
            stop_time = array[key_v][list(array[key_v].keys())[-1]]
    array[key_v][len(arrays[i])] = stop_time
    print(f'{len(arrays[i])} elements - {key_v}')

# LIST
for i in range(len(arrays)):
    my_list = List()
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_list.add_sorted(arrays[i][j])
    add_time_to_result_array('add_to_list', s_time)

    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_list.find(arrays[i][j])
    add_time_to_result_array('find_in_list', s_time)

    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_list.find(arrays[i][j])
    add_time_to_result_array('delete_in_list', s_time)
    print()
    


# BST
for i in range(len(arrays)):
    my_BST = BinarySearchTree()
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_BST.add(TreeElement(arrays[i][j]))
    add_time_to_result_array('add_to_BST', s_time)
    
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_BST.find(arrays[i][j])
    add_time_to_result_array('find_in_BST', s_time)

    s_time = time_ns()
    for j in range(len(arrays[i]) - 1, 0, -1):
        my_BST.find(arrays[i][j])
    add_time_to_result_array('delete_in_BST', s_time)
    print()


# AVL
for i in range(len(arrays)):
    my_BST = BinarySearchTree()
    my_AVL = BinarySearchTree()
    print(f'{len(arrays[i])} elements - add_to_BST')
    s_time = time_ns()
    for j in range(len(arrays[i])):
        my_BST.add(TreeElement(arrays[i][j]))
    results['get_height_of_BST'][len(arrays[i])] = my_BST.find_height()
    
    my_AVL.first_el = create_avl(my_BST.get_inorder())
    results['get_height_of_AVL'][len(arrays[i])] = my_AVL.find_height()
    
trans1 = []
for i in range(len(arrays)):
    trans1.append([len(arrays[i]), 
                   results['add_to_list'][len(arrays[i])], results['add_to_BST'][len(arrays[i])], 
                   results['find_in_list'][len(arrays[i])], results['find_in_BST'][len(arrays[i])],
                   results['delete_in_list'][len(arrays[i])], results['delete_in_BST'][len(arrays[i])]])

trans2 = []
for i in range(len(arrays)):
    trans2.append([len(arrays[i]), results['get_height_of_BST'][len(arrays[i])], results['get_height_of_AVL'][len(arrays[i])]])

df1 = pd.DataFrame(trans1, columns=['COUNT', 'add_to_list', 'add_to_BST', 'find_in_list', 'find_in_BST', 'delete_in_list', 'delete_in_BST'])
df2 = pd.DataFrame(trans2, columns=['COUNT', 'get_height_of_BST', 'get_height_of_AVL'])

with pd.ExcelWriter('Result.xlsx', engine='xlsxwriter') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
    worksheet = writer.sheets['Sheet1']

    workbook = writer.book
    chart1 = workbook.add_chart({'type': 'line'})
    chart1.add_series({
        'name':         'Add List',
        'categories':   f'=Sheet1!$A$2:$A${len(arrays) + 1}',
        'values':       f'=Sheet1!$B$2:$B${len(arrays) + 1}',
        'line':         {'color': 'red'}
    })
    chart1.add_series({
        'name':         'Add BST',
        'categories':   f'=Sheet1!$A$2:$A${len(arrays) + 1}',
        'values':       f'=Sheet1!$C$2:$C${len(arrays) + 1}',
        'line':         {'color': 'blue'}
    })

    chart1.set_title({'name': 'Adding elements to List vs Adding elements to BST'})
    chart1.set_x_axis({'name': 'Count'})
    chart1.set_y_axis({'name': 'Time (s)', 'log_base': 10})
    chart1.set_legend({'position': 'bottom'})

    chart2 = workbook.add_chart({'type': 'line'})
    chart2.add_series({
        'name':         'Find elements in List',
        'categories':   f'=Sheet1!$A$2:$A${len(arrays) + 1}',
        'values':       f'=Sheet1!$D$2:$D${len(arrays) + 1}',
        'line':         {'color': 'red'}
    })
    chart2.add_series({
        'name':         'Find elements in BST',
        'categories':   f'=Sheet1!$A$2:$A${len(arrays) + 1}',
        'values':       f'=Sheet1!$E$2:$E${len(arrays) + 1}',
        'line':         {'color': 'blue'}
    })

    chart2.set_title({'name': 'Find in List vs Find in BST'})
    chart2.set_x_axis({'name': 'Count'})
    chart2.set_y_axis({'name': 'Time (s)', 'log_base': 10})
    chart2.set_legend({'position': 'bottom'})

    chart3 = workbook.add_chart({'type': 'line'})
    chart3.add_series({
        'name':         'Delete in List',
        'categories':   f'=Sheet1!$A$2:$A${len(arrays) + 1}',
        'values':       f'=Sheet1!$F$2:$F${len(arrays) + 1}',
        'line':         {'color': 'red'}
    })
    chart3.add_series({
        'name':         'Delete in BST',
        'categories':   f'=Sheet1!$A$2:$A${len(arrays) + 1}',
        'values':       f'=Sheet1!$G$2:$G${len(arrays) + 1}',
        'line':         {'color': 'blue'}
    })

    chart3.set_title({'name': 'Delete in List vs Delete in BST'})
    chart3.set_x_axis({'name': 'Count'})
    chart3.set_y_axis({'name': 'Time (s)', 'log_base': 10})
    chart3.set_legend({'position': 'bottom'})

    worksheet.insert_chart('K1', chart1)
    worksheet.insert_chart('S1', chart2)
    worksheet.insert_chart('K18', chart3)
    worksheet = writer.sheets['Sheet2']

