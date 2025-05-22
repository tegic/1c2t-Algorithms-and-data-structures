from binary_search_tree import TreeElement, BinarySearchTree

def create_avl(arr):
    return create_avl_recursive(arr)

def create_avl_recursive(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2
    el = TreeElement(arr[mid])
    el.less = create_avl_recursive(arr[:mid])
    el.more = create_avl_recursive(arr[mid+1:])

    return el