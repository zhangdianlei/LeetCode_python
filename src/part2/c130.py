# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/18 4:01 PM
"""


def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if board:

        queue = []

        for index, i in enumerate(board[0]):
            if i == "O":
                board[0][index] = "-"
                queue.append([0, index])

        for index, i in enumerate(board[-1]):
            if i == "O":
                board[len(board) - 1][index] = "-"
                queue.append([len(board) - 1, index])

        for i in range(len(board)):
            if board[i][0] == "O":
                board[i][0] = "-"
                queue.append([i, 0])

        for i in range(len(board)):
            if board[i][-1] == "O":
                board[i][len(board[0]) - 1] = "-"
                queue.append([i, len(board[0]) - 1])

        while queue:
            top = queue.pop(0)
            x, y = top[0], top[1]
            # 上下左右添加
            if x - 1 > 0 and board[x - 1][y] == "O":
                board[x - 1][y] = "-"
                queue.append([x - 1, y])
            if x + 1 < len(board) and board[x + 1][y] == "O":
                board[x + 1][y] = "-"
                queue.append([x + 1, y])
            if y - 1 > 0 and board[x][y - 1] == "O":
                board[x][y - 1] = "-"
                queue.append([x, y - 1])
            if y + 1 < len(board[0]) and board[x][y + 1] == "O":
                board[x][y + 1] = "-"
                queue.append([x, y + 1])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "-":
                    board[i][j] = "O"

        print(queue)
        return board


if __name__ == '__main__':
    board = [
        ["X", "O", "X", "X", "X"],
        ["X", "X", "O", "X", "O"],
        ["O", "X", "X", "X", "X"],
        ["X", "X", "O", "X", "X"]
    ]

    board = [
    ]

    board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

    print(solve(board))
