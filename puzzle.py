"""
Mykola Kryvyi
Lab 0.2
Github: https://github.com/mykolakryvyi/pazzle.git
"""

def check_row_unique(board):
    """
    (list) -> (bool)
    Function checks first condition, i.e. unique numbers in each row

    >>> check_row_unique(["**** ****","***1 ****","**  3****",\
"* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    for i in range(9):
        row = board[i]
        lst_of_digits = []
        for j in row:
            try:
                digit = int(j)
                lst_of_digits.append(digit)
            except ValueError:
                continue
        #check whether there are any repests of digits
        if len(lst_of_digits)!=len(set(lst_of_digits)):
            return False
        lst_of_digits.clear()
    return True

def check_column_unique(board):
    """
    (list) -> (bool)
    Function checks second condition, i.e. unique numbers in each column

    >>> check_column_unique(["**** ****","***1 ****","**  3****",\
"* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    """
    for i in range(9):
        lst_of_digits = []
        for j in range(9):
            try:
                digit = int(board[j][i])
                lst_of_digits.append(digit)
            except ValueError:
                continue
        if len(lst_of_digits)!=len(set(lst_of_digits)):
            return False
        lst_of_digits.clear()
    return True

def check_colour_unique(board):
    """
    (list) -> (bool)
    Function checks third condition, i.e. unique numbers in each colourful block

    >>> check_colour_unique(["**** ****","***1 ****","**  3****",\
"* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    for j in range(9):
        lst_of_digits = []
        #first loop, looking for 'cut' columns
        for i in range(0,9 - j - 1):
            try:
                digit = int(board[i][j])
                lst_of_digits.append(digit)
            except ValueError:
                continue
        #second loop, looking for 'cut' rows
        for i in range(j, 9):
            try:
                digit = int(board[9 - j - 1][i])
                lst_of_digits.append(digit)
            except ValueError:
                continue
        if len(lst_of_digits)!=len(set(lst_of_digits)):
            return False
        lst_of_digits.clear()
    return True

def validate_board(board):
    """
    (list) -> (bool)
    Function checks all previous conditions

    >>> validate_board(["**** ****","***1 ****","**  3****",\
"* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    """
    return check_row_unique(board) and check_column_unique(board) and check_colour_unique(board)
