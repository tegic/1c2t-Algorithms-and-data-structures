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
    def __init__(self, first_el):
        self.first_el = first_el

