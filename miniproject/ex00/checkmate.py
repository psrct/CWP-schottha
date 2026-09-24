#!/usr/bin/python3

piece = "PBRQK"

def parse_board(board):
    # ฟังก์ชัน แปลงจากข้อความตารางยาวเป็น list แบ่งตามบรรทัด
    rows = board.split("\n")
    grid = []
    for row in rows:
        newlist = []
        for i in range(0, len(row)):
            newlist.append(row[i])
        grid.append(newlist)
    return grid

def is_valid_board(grid):
    # 1.เช็คจำนวนแถว == ความยาวแต่ละแถว(ต้องไม่มีแถวไหนไม่เท่า)
    num_rows = len(grid)
    if num_rows == 0:
        return False
    for row in grid:
        if len(row) != num_rows:
            return False
    # 2.เช็คทีละเซลว่ามีคิงมั้ย หากมี +=1 เมื่อครบเช็คว่า มีแค่ตัวเดียวมั้ย
    num_kings = 0
    for row in grid:
        for cell in row:
            if cell == "K":
                num_kings += 1
    if num_kings != 1:
        return False
    return True

def find_king(grid):
    # หาตัวคิงแล้วเก็บ index King ไว้
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "K":
                king_pos = (i,j)
                # print(f"{i}{j} = {cell}")
                return king_pos

def check_straight_lines(grid, king_pos):
    # เช็ค ไลน์เดินทางตรงของหมาก R,Q
    king_row, king_col = king_pos
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != "R" and cell != "Q":
                continue
            if i == king_row:
                step = 1 if j > king_col else -1
                path = range(king_col + step, j, step)
                blocked = any(grid[i][c] in piece for c in path)
                if not blocked:
                    return True
            elif j == king_col:
                step = 1 if i > king_row else -1
                path = range(king_row + step, i, step)
                blocked = any(grid[r][j] in piece for r in path)
                if not blocked:
                    return True
    return False

# def check_diagonal_lines(grid, king_pos):
    # เช็ค ไลน์เดินทแยงของหมาก P,Q
    
# def check_pawn(grid, king_pos):
    # เช็คไลน์เดินทแยงของหมาก B

# def checkmate(board):

grid = parse_board("""\
.R..
.K..
..P.
....\
""")
king_pos = find_king(grid)

print(check_straight_lines(grid, king_pos))
