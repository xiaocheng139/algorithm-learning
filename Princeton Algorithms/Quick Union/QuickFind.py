class QuickFindUF:
    # Time complexity: O(n)
    def __init__(self, N):
        self.id = list()
        for i in range(N):
            self.id[i] = i

    # Time complexity: O(1)
    def connected(self, p, q):
        return self.id[p] == self.id[q]

    # Time complexity: O(n)
    def union(self, p, q):
        pid, qid = self.id[p], self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid