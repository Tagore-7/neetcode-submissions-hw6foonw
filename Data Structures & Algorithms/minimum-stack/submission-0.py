class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minValue.append(min(self.minValue[-1] if self.minValue else val ,val))

    def pop(self) -> None:
        self.stack.pop()
        self.minValue.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValue[-1]
