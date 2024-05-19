class CustomStack:

    def __init__(self, maxSize: int):
        self.data = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.data) < self.max_size:
            self.data.insert(0, x)

    def pop(self) -> int:
        if len(self.data) == 0:
            return -1
        else:
            return self.data.pop(0)

    def increment(self, k: int, val: int) -> None:
        self.data = self.data[::-1]
        for i in range(min(len(self.data), k)):
            self.data[i] += val
        self.data = self.data[::-1]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
