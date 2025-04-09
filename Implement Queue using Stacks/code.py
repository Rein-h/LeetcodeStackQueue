"""Implement Queue using Stacks"""


class MyQueue:
    """Class for representing MyQueue"""

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it.
        """
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        """
        Returns the element at the front of the queue.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns true if the queue is empty, false otherwise.
        """
        return not self.input and not self.output
