class Solution(object):
        def setZeroes(self, matrix):
            ROWS, COLS = len(matrix), len(matrix[0])
            first_col_has_zero = False

            for r in range(ROWS):
                if matrix[r][0] == 0:
                    first_col_has_zero = True
                for c in range(1, COLS):
                    if matrix[r][c] == 0:
                        matrix[0][c] = 0
                        matrix[r][0] = 0

            for r in range(1, ROWS):
                for c in range(1, COLS):
                    if matrix[0][c] == 0 or matrix[r][0] == 0:
                        matrix[r][c] = 0

            if matrix[0][0] == 0:
                for c in range(COLS):
                    matrix[0][c] = 0

            if first_col_has_zero:
                for r in range(ROWS):
                    matrix[r][0] = 0

        