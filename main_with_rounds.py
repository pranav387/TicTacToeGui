import playsound as playsound
from TicTacToeGui import TicTacToeAlgorithm
import tkinter as tk
from tkinter import messagebox

board = [" "] * 9
root = tk.Tk()
root.iconbitmap("Untitled.ico")
root.geometry("300x300")
root.resizable(False, False)
rounds = 1
root.title(f"[Round {rounds}]Tic Tac Toe GUI by Pranav Karthik")
x_turn = True

playsound.playsound('stranger-things.mp3',block=False)

def next_round():
    global rounds
    global board
    global x_turn
    rounds += 1
    root.title(f"Round {rounds}")
    board = [" "] * 9
    x_turn = True
    button1['text'] = " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " "
def button1_func():
    global x_turn
    if x_turn:
        board[0] = "X"
        button1['text'] = "X"
        x_turn = False
    else:
        board[0] = "Y"
        button1['text'] = "O"
        x_turn = True
    check = TicTacToeAlgorithm(board)
    if check.check_x_won():
        messagebox.showinfo("Winner", "Congratulations Player 1, Your team(X) has won the game!")
        next_round()
    elif check.check_y_won():
        messagebox.showinfo("Winner", "Congratulations Player 2, Your team(O or Y) has won the game!")
        next_round()
    elif check.check_draw():
        messagebox.showinfo("Draw!", "Well played players! Unfortunately it is a draw!")
        next_round()

def button2_func():
    global x_turn
    if x_turn:
        board[1] = "X"
        button2['text'] = "X"
        x_turn = False
    else:
        board[1] = "Y"
        button2['text'] = "O"
        x_turn = True
    check = TicTacToeAlgorithm(board)
    if check.check_x_won():
        messagebox.showinfo("Winner", "Congratulations Player 1, Your team(X) has won the game!")
        next_round()
    elif check.check_y_won():
        messagebox.showinfo("Winner", "Congratulations Player 2, Your team(O or Y) has won the game!")
        next_round()
    elif check.check_draw():
        messagebox.showinfo("Draw!", "Well played players! Unfortunately it is a draw!")
        next_round()

def button3_func():
    global x_turn
    if x_turn:
        board[2] = "X"
        button3['text'] = "X"
        x_turn = False
    else:
        board[2] = "Y"
        button3['text'] = "O"
        x_turn = True
    check = TicTacToeAlgorithm(board)
    if check.check_x_won():
        messagebox.showinfo("Winner", "Congratulations Player 1, Your team(X) has won the game!")
        next_round()
    elif check.check_y_won():
        messagebox.showinfo("Winner", "Congratulations Player 2, Your team(O or Y) has won the game!")
        next_round()
    elif check.check_draw():
        messagebox.showinfo("Draw!", "Well played players! Unfortunately it is a draw!")
        next_round()

def button4_func():
    global x_turn
    if x_turn:
        board[3] = "X"
        button4['text'] = "X"
        x_turn = False
    else:
        board[3] = "Y"
        button4['text'] = "O"
        x_turn = True
    check = TicTacToeAlgorithm(board)
    if check.check_x_won():
        messagebox.showinfo("Winner", "Congratulations Player 1, Your team(X) has won the game!")
        next_round()
    elif check.check_y_won():
        messagebox.showinfo("Winner", "Congratulations Player 2, Your team(O or Y) has won the game!")
        next_round()
    elif check.check_draw():
        messagebox.showinfo("Draw!", "Well played players! Unfortunately it is a draw!")
        next_round()

def button5_func():
    global x_turn
    if x_turn:
        board[4] = "X"
        button5['text'] = "X"
        x_turn = False
    else:
        board[4] = "Y"
        button5['text'] = "O"
        x_turn = True
    check = TicTacToeAlgorithm(board)
    if check.check_x_won():
        messagebox.showinfo("Winner", "Congratulations Player 1, Your team(X) has won the game!")
        next_round()
    elif check.check_y_won():
        messagebox.showinfo("Winner", "Congratulations Player 2, Your team(O or Y) has won the game!")
        next_round()
    elif check.check_draw():
        messagebox.showinfo("Draw!", "Well played players! Unfortunately it is a draw!")
        next_round()

def button6_func():
    global x_turn
    if x_turn:
        board[5] = "X"
        button6['text'] = "X"
        x_turn = False
    else:
        board[5] = "Y"
        button6['text'] = "O"
        x_turn = True
    check = TicTacToeAlgorithm(board)
    if check.check_x_won():
        messagebox.showinfo("Winner", "Congratulations Player 1, Your team(X) has won the game!")
        next_round()
    elif check.check_y_won():
        messagebox.showinfo("Winner", "Congratulations Player 2, Your team(O or Y) has won the game!")
        next_round()
    elif check.check_draw():
        messagebox.showinfo("Draw!", "Well played players! Unfortunately it is a draw!")
        next_round()

def button7_func():
    global x_turn
    if x_turn:
        board[6] = "X"
        button7['text'] = "X"
        x_turn = False
    else:
        board[6] = "Y"
        button7['text'] = "O"
        x_turn = True
    check = TicTacToeAlgorithm(board)
    if check.check_x_won():
        messagebox.showinfo("Winner", "Congratulations Player 1, Your team(X) has won the game!")
        next_round()
    elif check.check_y_won():
        messagebox.showinfo("Winner", "Congratulations Player 2, Your team(O or Y) has won the game!")
        next_round()
    elif check.check_draw():
        messagebox.showinfo("Draw!", "Well played players! Unfortunately it is a draw!")
        next_round()

def button8_func():
    global x_turn
    if x_turn:
        board[7] = "X"
        button8['text'] = "X"
        x_turn = False
    else:
        board[7] = "Y"
        button8['text'] = "O"
        x_turn = True
    check = TicTacToeAlgorithm(board)
    if check.check_x_won():
        messagebox.showinfo("Winner", "Congratulations Player 1, Your team(X) has won the game!")
        next_round()
    elif check.check_y_won():
        messagebox.showinfo("Winner", "Congratulations Player 2, Your team(O or Y) has won the game!")
        next_round()
    elif check.check_draw():
        messagebox.showinfo("Draw!", "Well played players! Unfortunately it is a draw!")
        next_round()

def button9_func():
    global x_turn
    if x_turn:
        board[8] = "X"
        button9['text'] = "X"
        x_turn = False
    else:
        board[8] = "Y"
        button9['text'] = "O"
        x_turn = True
    check = TicTacToeAlgorithm(board)
    if check.check_x_won():
        messagebox.showinfo("Winner", "Congratulations Player 1, Your team(X) has won the game!")
        next_round()
    elif check.check_y_won():
        messagebox.showinfo("Winner", "Congratulations Player 2, Your team(O or Y) has won the game!")
        next_round()
    elif check.check_draw():
        messagebox.showinfo("Draw!", "Well played players! Unfortunately it is a draw!")
        next_round()

button1 = tk.Button(root, text=" ", padx=2, pady=2, font=('Helvetica', '30'), command=button1_func)
button1.place(x=0, y=0, height=100, width=100)

button2 = tk.Button(root, text=" ", padx=2, pady=2, font=('Helvetica', '30'), command=button2_func)
button2.place(x=100, y=0, height=100, width=100)

button3 = tk.Button(root, text=" ", padx=2, pady=2, font=('Helvetica', '30'), command=button3_func)
button3.place(x=200, y=0, height=100, width=100)

button4 = tk.Button(root, text=" ", padx=2, pady=2, font=('Helvetica', '30'), command=button4_func)
button4.place(x=0, y=100, height=100, width=100)

button5 = tk.Button(root, text=" ", padx=2, pady=2, font=('Helvetica', '30'), command=button5_func)
button5.place(x=100, y=100, height=100, width=100)

button6 = tk.Button(root, text=" ", padx=2, pady=2, font=('Helvetica', '30'), command=button6_func)
button6.place(x=200, y=100, height=100, width=100)

button7 = tk.Button(root, text=" ", padx=2, pady=2, font=('Helvetica', '30'), command=button7_func)
button7.place(x=0, y=200, height=100, width=100)

button8 = tk.Button(root, text=" ", padx=2, pady=2, font=('Helvetica', '30'), command=button8_func)
button8.place(x=100, y=200, height=100, width=100)

button9 = tk.Button(root, text=" ", padx=2, pady=2, font=('Helvetica', '30'), command=button9_func)
button9.place(x=200, y=200, height=100, width=100)

root.mainloop()
