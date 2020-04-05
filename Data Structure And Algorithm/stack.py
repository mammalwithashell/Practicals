class stack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        if len(self.arr) == 0:
            return None
        else:
            return self.arr.pop()

    def isEmpty(self):
        return len(self.arr) == 0

    def peek(self):
        if len(self.arr) == 0:
            return None
        else:
            return self.arr[-1]
