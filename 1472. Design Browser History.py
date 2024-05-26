class BrowserHistory:

    def __init__(self, homepage: str):
        self.forward_history = []
        self.backward_history = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.backward_history = self.backward_history[:self.pos+1]
        self.backward_history.append(url)
        self.pos = len(self.backward_history) - 1

    def back(self, steps: int) -> str:
        if self.pos - steps < 0:
            self.pos = 0
        else:
            self.pos -= steps

        return self.backward_history[self.pos]

    def forward(self, steps: int) -> str:
        if self.pos + steps > len(self.backward_history) - 1:
            self.pos = len(self.backward_history) - 1
        else:
            self.pos += steps

        print(self.pos)
        print(len(self.backward_history))
        return self.backward_history[self.pos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
