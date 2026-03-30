class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        sub_mat = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                # Item exist in row already
                if val in rows_set[i]:
                    return False

                rows_set[i].add(val)

                # Item exist in column already
                if val in cols_set[j]:
                    return False

                cols_set[j].add(val)

                # Calculate the sub-matrix index
                idx = (i // 3) * 3 + (j // 3)

                if val in sub_mat[idx]:
                    return False

                sub_mat[idx].add(val)

        
        return True



                

                

        