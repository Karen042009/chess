import tkinter as tk
import piece

butten_1 = None


def f(butten_2):
    global butten_1
    if butten_1 is None:
        butten_1 = butten_2
    else:
        info = butten_1.grid_info()
        row = info["row"]
        column = info["column"]
        ss = [row, column]

        info = butten_2.grid_info()
        r = info["row"]
        c = info["column"]
        aa = [r, c]

        if piece.cek_move(ss, aa):
            move_1(butten_1, butten_2)
            butten_1 = None
        else:
            pass


def move_1(knopka_1, knopka_2):
    text1, bg1, fg1 = knopka_1["text"], knopka_1["bg"], knopka_1["fg"]
    knopka_1["text"], knopka_1["bg"], knopka_1["fg"] = (
        knopka_2["text"],
        knopka_2["bg"],
        knopka_2["fg"],
    )
    knopka_2["text"], knopka_2["bg"], knopka_2["fg"] = text1, bg1, fg1
    knopka_1["text"] = "    "


def chess_board(win):
    for i in range(8):
        for j in range(8):
            bg_color = "white" if (i + j) % 2 == 0 else "#696969"
            frame = tk.Frame(win, width=100, height=100, bg=bg_color)
            frame.grid(row=i, column=j)
