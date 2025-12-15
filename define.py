import curses
import clock
import time

## Inisialisasi & Tools untuk Windows
# Fungsi untuk membuat windows dengan persentase tertentu dari windows utama
def newWin(h,w,size_h,size_w,y,x):
    if h % 2 == 1:
        h -= 1

    new_h = int(h * size_h)
    new_w = int(w * size_w)
    new_y = int(h * y)
    new_x = int(w * x)

    return curses.newwin(new_h, new_w, new_y, new_x)

# List Windows yang dibuat
def listWin(stdscr):
    h, w = stdscr.getmaxyx()
    master = newWin(h, w, 1.00, 0.60, 0.00, 0.00)
    sub_master = master.derwin(master.getmaxyx()[0] - 4, master.getmaxyx()[1] - 8, 2, 4)
    waktu = newWin(h, w, 0.50, 0.41, 0.00, 0.60)
    menu = newWin(h, w, 0.50, 0.41, 0.50, 0.60)
    sub_menu = menu.derwin(3, 6, menu.getmaxyx()[0] // 2 - 3 // 2, menu.getmaxyx()[1] // 2 - 6 // 2)

    return master, waktu, menu, sub_master, sub_menu

# refresh seluruh windows
def refreshAllWin(stdscr, master, waktu, menu):
    stdscr.refresh() # Keseluruhan Windows
    master.refresh() # Hanya master Windows
    waktu.refresh() # Hanya waktu Windows 
    menu.refresh() # Hanya menu Windows

# untuk menampilkan metadata windows
def winMetadata(screen, title, keydesc, current_pos):
    screen.erase()
    screen.box()

    # untuk menulis Judul ke windows
    if title == '-':
        pass
    else:
        screen.addstr(0, 1, f" {title} ", curses.color_pair(5))

    # untuk menulis keterangan Key ke windows
    if keydesc == '-':
        pass
    else:
        x = 2
        for i in range(len(keydesc[0])):
            screen.addstr(screen.getmaxyx()[0] - 1, x, f" {keydesc[0][i][0]} {keydesc[0][i][2]} ", curses.color_pair(7))
            screen.addstr(screen.getmaxyx()[0] - 1, x+2, f"{keydesc[0][i][1]}", curses.color_pair(5))
            screen.addstr(screen.getmaxyx()[0] - 1, x+5, f"{keydesc[1][i]} ", curses.color_pair(1))
            x = x + 5 + len(keydesc[1][i]) + 3

    # untuk menulis posisi halaman ke windows
    if current_pos == '-':
        pass
    else:
        screen.addstr(0, 3 + len(title), f"{current_pos[0]} {current_pos[1]} ", curses.color_pair(7))
        screen.addstr(0, 3 + len(title) + len(str(current_pos[0])), "/", curses.color_pair(5))

## Modul Windows
# modul lampu indikator untuk memudahkan pengguna saat pengisian angket berlangsung
def indikatorAngket(screen, title, cf_values):
    screen.erase()
    screen.box()

    # menulis Judul ke windows
    if title == '-':
        pass
    else:
        screen.addstr(0, 1, f" {title} ", curses.color_pair(5))

    # Menulis indikator angket ke windows
    for i in range(4):
        current_char = i
        start = current_char * 5

        y = screen.getmaxyx()[0] // 2 - 7 // 2 + (i+i)
        x = screen.getmaxyx()[1] // 2 - 29 // 2

        for j in range(5):
            kode = f"G{start+j+1:02d}"
            cf_val = cf_values.get(kode, 0.0)
            cf_percen = convertPercentage(cf_val, 1)

            atribute = 0
            if cf_percen == 50:
                atribute = curses.color_pair(1) | curses.A_BOLD
            if cf_percen > 50:
                atribute = curses.color_pair(2) | curses.A_BOLD
            if cf_percen < 50:
                atribute = curses.color_pair(3) | curses.A_BOLD

            screen.addstr(y, x, "[   ]")
            screen.addstr(y, x+1, kode, atribute)
            x += 6

# modul Jam digital
def digitalClock(screen, title):
    screen.erase()
    screen.box()

    # menulis Judul ke Windows
    if title == '-':
        pass
    else:
        screen.addstr(0, 1, f" {title} ", curses.color_pair(5))

    # menentukan berapa ukuran dan dimana posisi jam di tulis
    ax = screen.getmaxyx()[1] // 2 - len(clock.getClockFormatShape(0)) // 2
    bx = screen.getmaxyx()[1] // 2 - len(time.strftime("%A, %d %B %Y", time.localtime())) // 2
    y = screen.getmaxyx()[0] // 2 - 7 // 2 - 1

    # menulis jam digital
    for i in range(7):
        new_ax = ax
        new_shape = clock.getClockFormatShape(i)

        for new_shape_char in str(new_shape):
            atribute = 0
            if new_shape_char == '-':
                atribute = curses.color_pair(1) | curses.A_DIM
            elif new_shape_char == '@':
                atribute = curses.color_pair(7) | curses.A_BOLD

            screen.addch(y + i, new_ax, new_shape_char, atribute)
            new_ax += 1

    # Menulis Keterangan Hari, Tanggal Bulan Tahun
    screen.addstr(y+7, bx, time.strftime("%A, %d %B %Y", time.localtime()))

# Modul menu pilihan
def menuSelection(menu_selection, current_row, screen, title):
    screen.erase()
    screen.box()

    # menulis Judul ke windows
    if title == '-':
        pass
    else:
        screen.addstr(0, 1, f" {title} ", curses.color_pair(5))

    # menulis keterangan key ke windows
    x = 2
    keydesc = [ ["↑", "↓", "Enter"], ["Up", "Down", "Select"] ]
    for i in range(len(keydesc[0])):
        screen.addstr(screen.getmaxyx()[0] - 1, x, " (", curses.color_pair(7))
        screen.addstr(screen.getmaxyx()[0] - 1, x+2, f"{keydesc[0][i]}", curses.color_pair(5))
        screen.addstr(screen.getmaxyx()[0] - 1, x+2+len(keydesc[0][i]), ") ", curses.color_pair(7))
        screen.addstr(screen.getmaxyx()[0] - 1, x+4+len(keydesc[0][i]), f"{keydesc[1][i]} ", curses.color_pair(1))
        x = x + 5 + len(keydesc[1][i]) + 3

    # menulis menu pilihan ke windows
    for idx, item in enumerate(menu_selection):
        x = screen.getmaxyx()[1] // 2 - len(item) // 2
        y = screen.getmaxyx()[0] // 2 - len(menu_selection) // 2 + idx
        if idx == current_row:
            screen.attron(curses.A_REVERSE)
            screen.addstr(y, x, item)
            screen.attroff(curses.A_REVERSE)
        else:
            screen.addstr(y, x, item)

# Modul Certainity Factor Roll
def cfRoll(screen, sub_screen, cf_values):
    screen.erase()
    screen.box()

    # menulis Judul Ke windows
    screen.addstr(0,1," Certainity Factor Roll ", curses.color_pair(5))

    # menulis keterangan key ke windows
    x = 2
    keydesc = [ ["(←)", "(↑)", "(→)", "(↓)"], ["-10%", "+1%", "+10%", "-1%"] ]
    for i in range(len(keydesc[0])):
        screen.addstr(screen.getmaxyx()[0] - 1, x, f" {keydesc[0][i][0]} {keydesc[0][i][2]} ", curses.color_pair(7))
        screen.addstr(screen.getmaxyx()[0] - 1, x+2, f"{keydesc[0][i][1]}", curses.color_pair(5))
        screen.addstr(screen.getmaxyx()[0] - 1, x+5, f"{keydesc[1][i]} ", curses.color_pair(1))
        x = x + 5 + len(keydesc[1][i]) + 3

    # Menulis cfRoll ke windows
    cf_percen = convertPercentage(cf_values, 1)
    sub_screen.box()
    sub_screen.addstr(1, 1, f"{cf_percen}%")

## Error Handler
# untuk mengatasi layar terlalu kecil
def errorLayarKecil(screen, lines, cols):
    errorKecil = "Layar Terlalu Kecil"
    while screen.getmaxyx()[0] < lines or screen.getmaxyx()[1] < cols:
        screen.erase()
        h, w = screen.getmaxyx()

        y = h // 2 - 1 // 2
        x = w // 2 - len(errorKecil) // 2

        screen.box()
        screen.addstr(y, x, errorKecil)
        screen.getch()

## Rumus dan Kalkulator
# aturan cf menurut para ahli
CF_RULES = {
    "G01": [("K03", 0.65), ("K04", 0.8)],
    "G02": [("K04", 0.9)],
    "G03": [("K04", 0.9)],
    "G04": [("K03", 0.7), ("K06", 0.55)],
    "G05": [("K01", 0.6), ("K02", 0.8)],
    "G06": [("K05", 0.9)],
    "G07": [("K01", 0.8)],
    "G08": [("K03", 0.75), ("K06", 0.6)],
    "G09": [("K03", 0.4), ("K06", 0.7)],
    "G10": [("K02", 0.9)],
    "G11": [("K01", 0.8), ("K02", 0.75)],
    "G12": [("K04", 1.0)],
    "G13": [("K06", 0.7)],
    "G14": [("K04", 0.9)],
    "G15": [("K01", 0.7), ("K05", 0.65)],
    "G16": [("K06", 0.9)],
    "G17": [("K06", 0.8), ("K03", 0.45)],
    "G18": [("K02", 0.8)],
    "G19": [("K01", 0.6)],
    "G20": [("K01", 0.8), ("K02", 0.7)],
}

# mengkonvert antara percen dan decimal
def convertPercentage(cf_value, mode):
    # dari percen ke decimal
    if mode == 0:
        return int((cf_value - 50) / 50)
    # dari decimal ke percen
    elif mode == 1:
        return int((cf_value * 50) + 50)

# Rumus Kombinasi
def combine_cf(c1, c2):
    return c1 + c2 * (1 - c1)

# Kalkulasi cf_user secara keseluruhan
def calculate_cf(user_cf):
    result = {}

    for kode, cf_user in user_cf.items():
        if cf_user == 0:
            continue

        if kode not in CF_RULES:
            continue

        for kerusakan, expert_cf in CF_RULES[kode]:
            cf_val = expert_cf * cf_user

            if kerusakan not in result:
                result[kerusakan] = cf_val
            else:
                result[kerusakan] = combine_cf(result[kerusakan], cf_val)

    return result
