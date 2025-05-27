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
        i = 1
        current_el = self.first_el
        while current_el != None:
            print(f"Element {i}: {current_el.value}")
            current_el = current_el.next_el
            i += 1

    def add_sorted(self, value):
        if self.first_el == None:
            self.first_el = ListElement(value, None)
            return 0
        if self.first_el.value > value:
            second_el = self.first_el
            self.first_el = ListElement(value, second_el)
            return 0
        current_el = self.first_el
        while current_el.next_el != None and current_el.next_el.value < value:
            current_el = current_el.next_el
        current_el.next_el = ListElement(value, current_el.next_el)
    
    def find(self, value):
        current_el = self.first_el
        while current_el != None:
            if current_el.value == value:
                return int(1)
            current_el = current_el.next_el
        return int(0)
    
    def delete_first(self):
        if self.first_el != None:
            self.first_el = self.first_el.next_el
            return int(1)
        return int(0)
