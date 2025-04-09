class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stack = {}
        self.maxfreq = 0

    def push(self, val: int) -> None:
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
        max_val = self.stack[self.maxfreq].pop()
        self.freq[max_val] -= 1

        if not self.stack[self.maxfreq]:
            self.maxfreq -= 1

        return max_val
