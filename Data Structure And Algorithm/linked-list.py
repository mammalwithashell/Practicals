class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Element(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Element(value)

    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def get_position(self, position):
        # Position starts from 1
        if position <= 0:
            return None
        temp = self.head
        while position > 1 and temp:
            position -= 1
            temp = temp.next
        return temp  # Return None if Not found

    def insert(self, value, position):
        # insert b/w position and position - 1
        # get the previous node
        prevNode = self.get_position(position - 1)
        node = Element(value)
        if prevNode is None:
            node.next = self.head
            self.head = node
        else:
            node.next = prevNode.next
            prevNode.next = node

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
