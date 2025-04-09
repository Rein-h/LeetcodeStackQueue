"""Maximum Frequency Stack"""


class FreqStack:
    """Class for representing FreqStack"""

    def __init__(self):
        self.freq = {}
        self.stack = {}
        self.maxfreq = 0

    def push(self, val: int) -> None:
        """
        Pushes an integer val onto the top of the stack.
        """
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1

        current = self.freq[val]
        if current > self.maxfreq:
            self.maxfreq = current

        if current not in self.stack:
            self.stack[current] = []
        self.stack[current].append(val)


    def pop(self) -> int:
        """
        Removes and returns the most frequent element in the stack.
            If there is a tie for the most frequent element, the element
            closest to the stack's top is removed and returned.
        """
        max_val = self.stack[self.maxfreq].pop()
        self.freq[max_val] -= 1

        if not self.stack[self.maxfreq]:
            self.maxfreq -= 1

        return max_val
