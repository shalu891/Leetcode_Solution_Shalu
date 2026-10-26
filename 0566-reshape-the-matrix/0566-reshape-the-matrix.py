class Solution(object):
    def matrixReshape(self, mat, r, c):
        if not mat or not mat[0]:
            return mat
        
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flat = [elem for row in mat for elem in row]
        
        return [flat[i * c:(i + 1) * c] for i in range(r)]

        
        