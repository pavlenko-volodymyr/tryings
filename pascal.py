# -*- coding: utf-8 -*- 

def pascal(col_n, row_n):
    if col_n in [0, row_n]: return 1
    if row_n in [0, 1]: return 1
    prev_row = [1,1]
    curr_row = []
    curr_row_n = 2
    while curr_row_n <= row_n:
        curr_row.append(1)
        curr_col_n = 1
        while curr_col_n < curr_row_n:
            curr_row.append(prev_row[curr_col_n - 1] + prev_row[curr_col_n])
            curr_col_n += 1
        curr_row.append(1)
        prev_row = curr_row[:]
        curr_row = []
        curr_row_n += 1
    print prev_row
    return prev_row[col_n]

if __name__ == '__main__':
    print pascal(1, 6)
