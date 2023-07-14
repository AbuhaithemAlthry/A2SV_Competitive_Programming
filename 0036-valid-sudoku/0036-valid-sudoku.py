class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [[row[id] for row in board] for id in range(len(board[0]))] # transposition
        for row, row2 in zip(board, columns):
            for num, num2 in zip(row, row2):
                if (num.isdigit() and row.count(num) != 1) or (num2.isdigit() and row2.count(num2) != 1): 
                    return False

        temp_arr = []
        arr = [] 
        for num in range(0,9,3):
            for col in board:
                temp_arr.append(col[num:num+3])
        for num in range(0,27,3):
            arr.append(temp_arr[num:num+3])

        values_arr = []
        for quad in arr:
            temp_arr = [] 

            for row in quad: 
                temp_arr += row

            for value in temp_arr:
                if value.isdigit():
                    values_arr.append(temp_arr.count(value))

        if values_arr != []:
            if max(values_arr) > 1:
                return False

        return True