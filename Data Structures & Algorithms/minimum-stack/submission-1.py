class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        pop = self.stack.pop()

        if not self.stack:
            self.min = float('inf')
            return
        if pop == self.min:
            self.min = self.stack[0]
            for i in range(len(self.stack)):
                if self.stack[i] < self.min:
                    self.min = self.stack[i]


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min    
