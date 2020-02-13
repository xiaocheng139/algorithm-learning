class QuickUnion:
    # Time Complexity: O(n)
    def __init__(self, N):
        self.id = list()
        for i in range(N):
            self.id[i] = i

    # Time Complexity: O(n)
    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    # Time Complexity: O(n)
    def connected(self, p, q):
        return self.root(p) == self.root(q)

    # Time Complexity: O(n)
    def union(self, p, q):
        rootp = self.root(p)
        rpptq = self.root(q)
        self.id[rootp] = rpptq