class queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, value):
        self.arr.append(value)

    def dequeue(self):
        if len(self.arr) == 0:
            return None
        else:
            return self.arr.pop(0)

    def isEmpty(self):
        return len(self.arr) == 0

    def peek(self):
        if len(self.arr) == 0:
            return None
        else:
            return self.arr[0]
