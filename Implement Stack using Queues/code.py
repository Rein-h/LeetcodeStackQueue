"""Implement Stack using Queues"""


import collections

class MyStack:
    """Class for representing MyStack"""

    def __init__(self):
        self.output = collections.deque()

    def push(self, x: int) -> None:
        """
        Pushes element x to the top of the stack.
        """
        self.output.append(x)
        for _ in range(len(self.output) - 1):
            self.output.append(self.output.popleft())

    def pop(self) -> int:
        """
        Removes the element on the top of the stack and returns it.
        """
        return self.output.popleft()

    def top(self) -> int:
        """
        Returns the element on the top of the stack.
        """
        return self.output[0]

    def empty(self) -> bool:
        """
        Returns true if the stack is empty, false otherwise.
        """
        return not self.output
