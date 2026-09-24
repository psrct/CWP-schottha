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

def print_grid(grid):
    # print grid ทีละแถว
    lines = []
    for idx, row in enumerate(grid):
        row_str = "[" + " ".join(f"'{c}'" for c in row) + "]"
        prefix = "[" if idx == 0 else " "
        lines.append(prefix + row_str)
    lines[-1] += "]"
    print("\n".join(lines))

def get_board_size(grid):
    # (จำนวนแถว, จำนวนคอลัมน์)
    return (len(grid), len(grid[0]) if grid else 0)

def is_square(grid):
    # เช็คจำนวนแถว == ความยาวแต่ละแถว(ต้องไม่มีแถวไหนไม่เท่า)
    num_rows = len(grid)
    if num_rows == 0:
        return False
    for row in grid:
        if len(row) != num_rows:
            return False
    return True

def count_kings(grid):
    # นับจำนวน King บนกระดานทั้งหมด
    num_kings = 0
    for row in grid:
        for cell in row:
            if cell == "K":
                num_kings += 1
    return num_kings

def is_valid_board(grid):
    return is_square(grid) and count_kings(grid) == 1

def find_king(grid):
    # หาตัวคิงแล้วเก็บ index King ไว้
    for idr, row in enumerate(grid):
        for idc, cell in enumerate(row):
            if cell == "K":
                king_pos = (idr,idc)
                return king_pos

def check_straight_lines(grid, king_pos):
    # เช็ค ไลน์แนวทางตรงของหมาก R,Q
    king_row, king_col = king_pos
    for idr, row in enumerate(grid):
        for idc, cell in enumerate(row):
            if cell != "R" and cell != "Q":
                continue
            if idr == king_row:
                step = 1 if idc > king_col else -1 # 1 = ด้านซ้าย หาก idc > king_col และ -1 = ด้านขวา หาก idc < king_col
                path = range(king_col + step, idc, step) #ได้จำนวนที่ผ่านทาง เช่น [2,3]
                blocked = any(grid[idr][c] in piece for c in path) #วนเช็ค grid[row][2] และ grid[row][3] ว่ามีหมากใน piece มั้ย
                #ซึ่งผลจะเป็น [False, True] หากพบก็แปลว่าถูกบล็อค check king ไม่สำเร็จ return false
                if not blocked:
                    return True
            elif idc == king_col: #เหมือนกันแต่เป็นแนวตั้ง column
                step = 1 if idr > king_row else -1
                path = range(king_row + step, idr, step)
                blocked = any(grid[r][idc] in piece for r in path)
                if not blocked:
                    return True
    return False

def check_diagonal_lines(grid, king_pos):
    # เช็ค ไลน์แนวทแยงของหมาก B,Q
    king_row, king_col = king_pos
    for idr, row in enumerate(grid):
        for idc, cell in enumerate(row):
            if cell != "B" and cell != "Q":
                continue
            # อยู่แนวทแยงเดียวกันก็ต่อเมื่อระยะห่างแถว == ระยะห่างคอลัมน์
            # (idr == king_row กันเคส idc == king_col ด้วย ช่องเดียวกับ King พอดี)
            if idr == king_row or abs(idr - king_row) != abs(idc - king_col):
                continue
            # หาทิศทางเดินจาก King ไปหาหมาก ทีละแกน (ขึ้น/ลง, ซ้าย/ขวา)
            step_row = 1 if idr > king_row else -1
            step_col = 1 if idc > king_col else -1
            # ช่องคั่นกลางระหว่าง King กับหมาก (ไม่รวมทั้งสองปลาย) แยกเป็นแกนแถว/คอลัมน์
            rows_path = range(king_row + step_row, idr, step_row)
            cols_path = range(king_col + step_col, idc, step_col)
            # zip จับคู่ (row, col) ทีละตำแหน่งบนเส้นทแยงจริง แล้วเช็คว่ามีอะไรขวางไหม
            blocked = any(grid[r][c] in piece for r, c in zip(rows_path, cols_path))
            if not blocked:
                return True
    return False

def check_pawn(grid, king_pos):
    # เช็คไลน์เดินทแยงของหมาก P
    king_row, king_col = king_pos
    for idr, row in enumerate(grid):
        for idc, cell in enumerate(row):
            if cell != "P": #หา P ทีละเซลไม่เจอจะเข้าเงื่อนไข แต่เจอก็จะไป if ต่อไป
                continue
            if  (idr-1) == king_row: #เช็คหาว่า row ก่อนหน้ามี มี King ไหม
                if king_pos == ((idr-1),(idc-1)) or king_pos == ((idr-1),(idc+1)): #ถ้าตำแหน่ง king อยู่เยื้องบนซ้าย-ขวาไหม
                    return True
    return False

def build_check_range(grid):
    # สร้างกระดานเดียวกัน แต่ X ทับทุกช่องที่อยู่ในไลน์โจมตีของหมาก R,B,Q,P 
    # ตัวใดตัวหนึ่งบนกระดาน และจะหยุดมาร์คเมื่อโดนบัง
    num_rows, num_cols = get_board_size(grid)
    # copy กระดานออกมาแก้แทน ไม่แตะ grid ตัวจริง (row[:] copy ทีละแถว)
    marked = [row[:] for row in grid]
    # ทิศทางเป็น (delta_row, delta_col): บน/ล่าง/ซ้าย/ขวา และ 4 มุมทแยง
    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def mark_line(i, j, directions):
        # เดินหมากทีละทิศทาง ทีละ 1 ช่อง จนกว่าจะหลุดขอบกระดาน
        for dr, dc in directions:
            r, c = i + dr, j + dc
            while 0 <= r < num_rows and 0 <= c < num_cols:
                if marked[r][c] == ".":
                    marked[r][c] = "X"
                # เช็คจาก grid ตัวจริง (ไม่ใช่ marked ที่เพิ่งเติม X)
                # เพราะถ้าเช็คจาก marked จะเข้าใจผิดว่า X ที่เพิ่งมาร์คคือของขวางทาง
                # แล้วหยุดเดินตั้งแต่ก้าวแรก
                if grid[r][c] != ".":
                    break
                r += dr
                c += dc

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "R" or cell == "Q":
                mark_line(i, j, straight_dirs)
            if cell == "B" or cell == "Q":
                mark_line(i, j, diagonal_dirs)
            if cell == "P":
                for dr, dc in [(-1, -1), (-1, 1)]:
                    r, c = i + dr, j + dc
                    if 0 <= r < num_rows and 0 <= c < num_cols and marked[r][c] == ".":
                        marked[r][c] = "X"
    return marked

def checkmate(board):
    grid = parse_board(board)
    print_grid(grid)
    print(get_board_size(grid))
    if not is_square(grid):
        print("Error: Wrong Dimension")
        return
    if count_kings(grid) != 1:
        print("Error: K Unit -> Possible Number")
        return

    king_pos = find_king(grid)
    in_check = (
        check_straight_lines(grid, king_pos)
        or check_diagonal_lines(grid, king_pos)
        or check_pawn(grid, king_pos)
    )#หากตัวเช็คอันไหน return True ออกมา เท่ากับว่า Check คิงสำเร็จ
    print("Check Range:")
    print_grid(build_check_range(grid))
    if in_check:
        print("Success")
    else:
        print("Fail")
