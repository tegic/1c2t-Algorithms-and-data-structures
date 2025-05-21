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
