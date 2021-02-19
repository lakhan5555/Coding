class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ds = []
        

    def push(self, x: int) -> None:
        self.ds.append(x)
        

    def pop(self) -> None:
        self.ds.pop()
        

    def top(self) -> int:
        return self.ds[-1]
        

    def getMin(self) -> int:
        return min(self.ds)
