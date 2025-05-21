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
        current_el = first_el
        a = []
        b = []
        a.append(current_el)
        while True:
            for i in range(len(a)):
                if a[i] == None:
                    b
                    continue
                b.append(a[i].less, a[i].more)
            a = []
            continue_while = False
            for i in range(len(b)):
                print(b[i])
                a.append(b[i])
                if b[i] != None:
                    continue_while = True
            b = []
            if continue_while == False:
                break


my_BST = BinarySearchTree()
my_BST.add(TreeElement(5))
my_BST.add(TreeElement(1))
my_BST.add(TreeElement(3))
my_BST.add(TreeElement(10)
my_BST.add(TreeElement(7))
my_BST.add(TreeElement(2))
my_BST.print()
