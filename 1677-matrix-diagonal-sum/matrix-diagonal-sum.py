class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        t=0
        for i in range(n):
            t+=mat[i][i]
            if i!=n-1-i:
                t+=mat[i][n-1-i]
        return t