class ListElement:
    def __init__(self, value, next_el):
        self.value = value
        self.next_el = next_el
    
    def set_value(self, value):
        self.value = value

class List:
    def __init__(self):
        self.first_el = None

    def print(self):
        i = 0
        current_el = self.first_el
        while current_el != None:
            print(f"Element {i}: {current_el.value}")
            current_el = current_el.next_el
            i += 1

    def add(self, value):
        new_el = ListElement(value, self.first_el)
        self.first_el = new_el
