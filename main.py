import curses
import define as df
import content as ct

def main(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(True)
    curses.curs_set(0)

    # Set Color
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_RED, -1)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    curses.init_pair(5, curses.COLOR_YELLOW, -1)
    curses.init_pair(6, curses.COLOR_MAGENTA, -1)
    curses.init_pair(7, curses.COLOR_CYAN, -1)

    # Sesi Menu
    menu_session = 0
    # 0 = Main Menu
    # 1 = Panduan Singkat
    # 2 = Angket
    # 3 = Pre-Submit
    # 4 = Hasil Perhitungan

    # master windows
    current_pos = []
    menu_key = []

    # Menu selection
    main_windows = []
    menu_selection = []
    current_row = 0

    # Certainity Factor Roll
    current_question = 0
    cf_values = {f"G{i+1:02d}": 0.0 for i in range(20)}
    kode = ""

    # Pre-Submit Windows
    current_page = 0
 
    while True:
        # fallback jika ukuran terminal terlalu kecil
        if stdscr.getmaxyx()[0] >= 34 and stdscr.getmaxyx()[1] >= 119:
            master, waktu, menu, sub_master, sub_menu = df.listWin(stdscr) # inisialisasi windows

            # Drawing Windows
            if menu_session == 0:
                # membuat variabel sementara
                menu_selection = ct.main_menu()[0]
                main_windows = ct.main_menu()[1]
                menu_key = [["<q>"], ["Quit"]]

                # menentukan tampilan windows
                df.digitalClock(waktu, "Waktu")
                df.menuSelection(menu_selection, current_row, menu, "-")
                df.winMetadata(master, "Layar Utama", menu_key, "-")

                # menentukan konten windows
                if current_row == 0:
                    sub_master.addstr(2, 0, main_windows[0])
                elif current_row == 1:
                    sub_master.addstr(2, 0, main_windows[1])

            elif menu_session == 1:
                # membuat variabel sementara
                menu_selection = ct.angketMenuSelection(0)
                main_windows = ct.panduanSingkat()
                menu_key = [["(←)", "(→)"], ["Prev Page", "Next Page"]]
                current_pos = [current_page+1, "2"]

                # menentukan tampilan windows
                df.digitalClock(waktu, "Waktu")
                df.menuSelection(menu_selection, current_row, menu, "Apakah Anda Sudah Mengerti?")
                df.winMetadata(master, "Panduan Singkat", menu_key, current_pos)

                # menentukan konten windows
                sub_master.addstr(2, 0, main_windows[current_page])

            elif menu_session == 2:
                # membuat variabel sementara
                kode = f"G{current_question+1:02d}"
                question = ct.dataAngket()[0]
                menu_key = [["<q>", "<n>", "<b>", "<s>"], ["Back", "Next Page", "Prev Page", "Submit"]]
                current_pos = [current_question+1, "20"]

                # menentukan tampilan windows
                df.indikatorAngket(waktu, "Lampu Indikator", cf_values)
                df.cfRoll(menu, sub_menu, cf_values[kode])
                df.winMetadata(master, "Angket", menu_key, current_pos)

                # menentukan konten windows
                sub_master.addstr(sub_master.getmaxyx()[0] // 2 - 4 // 2, 1, question[current_question])

            elif menu_session == 3:
                # membuat variabel sementara
                kode = f"G{current_question+1:02d}"
                question = ct.dataAngket()[0]
                menu_selection = ct.angketMenuSelection(1)
                menu_key = [["(←)", "(→)"], ["Prev Page", "Next Page"]]
                current_pos = [current_page+1, "4"]

                # menentukan tampilan windows
                df.indikatorAngket(waktu, "Lampu Indikator", cf_values)
                df.menuSelection(menu_selection, current_row, menu, "Apakah Anda Yakin?")
                df.winMetadata(master, "Halaman", menu_key, current_pos)

                # menentukan konten windows
                ct.preSubmit(cf_values.copy(), question, current_page, sub_master)

            elif menu_session == 4:
                # membuat variabel sementara
                results = df.calculate_cf(cf_values)
                answer = ct.dataAngket()[1]
                menu_selection = ct.angketMenuSelection(2)

                # menentukan tampilan windows
                df.digitalClock(waktu, "Waktu")
                df.menuSelection(menu_selection, current_row, menu, "-")
                df.winMetadata(master, "Hasil Perhitungan Certainity Factor", "-", "-")

                # menentukan konten windows
                ct.hasilPerhitungan(sub_master, results, answer)

        else:
            # fallback jika layar terminal terlalu kecil
            df.errorLayarKecil(stdscr, 34, 119)
            stdscr.erase()
            master, waktu, menu, sub_master, sub_menu = df.listWin(stdscr)

        # refresh seluruh windows
        df.refreshAllWin(stdscr, master, waktu, menu)

        # menunggu tombol di tekan
        key = stdscr.getch()

        # Resizing Window
        if key == curses.KEY_RESIZE:
            if stdscr.getmaxyx()[0] < 34 and stdscr.getmaxyx()[1] < 119:
                df.errorLayarKecil(stdscr, 34, 119)
                stdscr.erase()
                master, waktu, menu, sub_master, sub_menu = df.listWin(stdscr)
            else:
                stdscr.erase()
                master, waktu, menu, sub_master, sub_menu = df.listWin(stdscr)

        # Key
        if menu_session == 0: # untuk sesi Menu Utama
            if key == ord('q'):
                break

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu_selection) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == 0:
                    menu_session = 1

        elif menu_session == 1: # untuk sesi Panduan Singkat
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu_selection) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == 0:
                    menu_session = 2
                    current_page = 0
                elif current_row == 1:
                    current_row = 0
                    current_page = 0
                    menu_session = 0

            if key == curses.KEY_LEFT and current_page > 0:
                current_page -= 1
            elif key == curses.KEY_RIGHT and current_page < 1:
                current_page += 1

        elif menu_session == 2: # untuk sesi Angket
            if key == ord('q'):
                menu_session = 0
                current_question = 0
                cf_values = {f"G{i+1:02d}": 0.0 for i in range(20)}
            elif key == ord('n') and current_question < 19:
                current_question += 1
            elif key == ord('b') and current_question > 0:
                current_question -= 1
            elif key == ord('s'):
                menu_session = 3

            if key == curses.KEY_UP:
                cf_values[kode] = min(1.0, cf_values[kode] + 0.02)
            elif key == curses.KEY_DOWN:
                cf_values[kode] = max(-1.0, cf_values[kode] - 0.02)
            elif key == curses.KEY_LEFT:
                cf_values[kode] = max(-1.0, cf_values[kode] - 0.2)
            elif key == curses.KEY_RIGHT:
                cf_values[kode] = min(1.0, cf_values[kode] + 0.2)

            if key == curses.KEY_ENTER or key in [10, 13]:
                if current_question == 19:
                    menu_session = 3
                elif current_question < 19:
                    current_question += 1
                elif current_question > 0:
                    current_question -= 1

        elif menu_session == 3: # untuk sesi Pre-Submit
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu_selection) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == 0:
                    menu_session = 4
                elif current_row == 1:
                    current_row = 0
                    menu_session = 2

            if key == curses.KEY_LEFT and current_page > 0:
                current_page -= 1
            elif key == curses.KEY_RIGHT and current_page < 3:
                current_page += 1

        elif menu_session == 4: # untuk sesi Hasil Perhitungan
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu_selection) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == 0:
                    current_page = 0
                    current_row = 0
                    current_question = 0
                    cf_values = {f"G{i+1:02d}": 0.0 for i in range(20)}
                    menu_session = 0

curses.wrapper(main) # untuk menjalankan curses
