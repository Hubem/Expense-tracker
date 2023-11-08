from tkinter import *
from tkinter.ttk import *

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

def main():
    root = Tk()
    root.geometry('250x200')
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)

    #Menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    type_menu = Menu(menubar, tearoff=False)
    type_menu.add_command(label='Groceries expenses')
    type_menu.add_command(label="Household expenses")
    type_menu.add_command(label="Entertainment expenses")
    type_menu.add_command(label="Other expenses")

    exit_menu = Menu(menubar, tearoff=0)
    exit_menu.add_command(label='Exit', command=root.destroy)

    menubar.add_cascade(label="Types", menu=type_menu)
    menubar.add_cascade(label="Other", menu=exit_menu)
    

    root.mainloop()

main()
