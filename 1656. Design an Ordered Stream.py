class OrderedStream:

    def __init__(self, n: int):
        self.pairs = [0] * n
        self.next_id = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.pairs[idKey - 1] = value
        output = []
        while self.next_id < len(self.pairs):
            if self.pairs[self.next_id] != 0:
                output.append(self.pairs[self.next_id])
                self.next_id += 1
            else:
                break
        return output

