# make a video about how I learned VIM and why I use it

class TreeElement():
    def __init__(self, value):
        self.value = value
        self.less = None
        self.more = None

    def set_less(self, value):
        self.less = value

    def set_more(self, value):
        self.more = value


class BinarySearchTree():
    def __init__(self):
        self.first_el = None

    def add(self, new_el):
        if self.first_el == None:
            self.first_el = new_el
            return 0
        current_el = self.first_el
        is_more = None
        while True:
            if new_el.value > current_el.value:
                if current_el.more == None:
                    is_more = True
                    break
                current_el = current_el.more
            else:
                if current_el.less == None:
                    is_more = False
                    break
                current_el = current_el.less
        if is_more == True:
            current_el.more = new_el
        else:
            current_el.less = new_el

    def print(self):
        current_el = self.first_el
        a = []
        b = []
        a.append(current_el)
        print(current_el.value)
        while True:
            for i in range(len(a)):
                if a[i] == None:
                    b.append(None)
                    b.append(None)
                    continue
                b.append(a[i].less)
                b.append(a[i].more)
            a = []
            continue_while = False
            for i in range(len(b)):
                if b[i] != None:
                    print(b[i].value, end='  ')
                else:
                    print('-', end='')
                a.append(b[i])
                if b[i] != None:
                    continue_while = True
            b = []
            print('')
            if continue_while == False:
                break
    
    def find(self, value):
        previous_el = None
        current_el = self.first_el
        while current_el != None:
            if current_el.value == value:
                return previous_el, current_el
            elif current_el.value < value:
                previous_el = current_el
                current_el = current_el.more
            elif current_el.value > value:
                previous_el = current_el
                current_el = current_el.less
        return False, False
    
    def find_min_el(self, start_el):
        # there is 100% smaller and bigger element
        previous_min_el = start_el
        min_el = start_el.more
        while min_el.less != None:
            previous_min_el = min_el
            min_el = min_el.less
        return min_el, previous_min_el

    def delete(self, value):
        previous_el, current_el = self.find(value)
        if previous_el == current_el == False:
            return False
        if current_el.less == None and current_el.more == None: # DONE
            if previous_el.value > current_el.value:
                previous_el.less = None
            else:
                previous_el.more = None
        elif current_el.less == None:                           # DONE
            if previous_el.value > current_el.value:
                previous_el.less = current_el.more
            else:
                previous_el.more = current_el.more
        elif current_el.more == None:                           # DONE
            if previous_el.value > current_el.value:
                previous_el.less = current_el.less
            else:
                previous_el.more = current_el.less
        else:                                                   # DONE
            min_el, previous_min_el = self.find_min_el(current_el)
            previous_min_el.less = min_el.more
            if previous_el.value > current_el.value:
                previous_min_el.less = min_el.more
                min_el.more = current_el.more
                min_el.less = current_el.less
                previous_el.less = min_el
            else:
                previous_el.more.value = min_el.value
                previous_min_el.less = min_el.more
        return True

if __name__ == '__main__':
    # For tests
    my_BST = BinarySearchTree()
    my_BST.add(TreeElement(5))
    my_BST.add(TreeElement(1))
    my_BST.add(TreeElement(3))
    my_BST.add(TreeElement(10))
    my_BST.add(TreeElement(7))
    my_BST.add(TreeElement(2))
    my_BST.print()