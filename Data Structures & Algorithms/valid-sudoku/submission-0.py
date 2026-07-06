class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_box_list = []
        sub_box_list.append(board[0][0:3] + board[1][0:3] + board[2][0:3])
        sub_box_list.append(board[0][3:6] + board[1][3:6] + board[2][3:6])
        sub_box_list.append(board[0][6:9] + board[1][6:9] + board[2][6:9])
        sub_box_list.append(board[3][0:3] + board[4][0:3] + board[5][0:3])
        sub_box_list.append(board[3][3:6] + board[4][3:6] + board[5][3:6])
        sub_box_list.append(board[3][6:9] + board[4][6:9] + board[5][6:9])
        sub_box_list.append(board[6][0:3] + board[7][0:3] + board[8][0:3])
        sub_box_list.append(board[6][3:6] + board[7][3:6] + board[8][3:6])
        sub_box_list.append(board[6][6:9] + board[7][6:9] + board[8][6:9])
        for sub_box in sub_box_list:
            sub_box_dict = {}
            for item in sub_box:
                if item == ".":
                    continue
                if item not in sub_box_dict:
                    sub_box_dict[item] = 1
                else:
                    return False
        for row in board:
            row_dict = {}
            for item in row:
                if item == ".":
                    continue
                if item not in row_dict:
                    row_dict[item] = 1
                else:
                    return False
        for column in range(len(board)):
            column_dict = {}
            for row in range(len(board)):
                item = board[row][column]
                if item == ".":
                    continue
                if item not in column_dict:
                    column_dict[item] = 1
                else:
                    return False
        return True

