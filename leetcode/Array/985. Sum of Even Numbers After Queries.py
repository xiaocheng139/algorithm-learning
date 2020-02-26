class Solution:
    def sumEvenAfterQueries(self, A, queries):
        res = []
        total = sum([i for i in A if i % 2 == 0])
        if not A:
            return 0

        for query in queries:
            if A[query[1]] % 2 == 0:
                total -= A[query[1]]
            A[query[1]] += query[0]
            if A[query[1]] % 2 == 0:
                total += A[query[1]]
            res.append(total)

        return res


solution = Solution()
print(solution.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))