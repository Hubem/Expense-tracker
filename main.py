from tkinter import *
from tkinter.ttk import *

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

    def delete(self, boxaile):
        myLabel=Label(boxaile, text="The chosen value was successfully deleted")
        myLabel.grid(row=4,column=0)

    def delete_expense(self, database,val1, val2, val3):
        name=val1.get()
        price=val2.get()
        date=val3.get()
        delete=database(name,price)
        return delete
    
    def inserted(self, boxaile):
        myLabel=Label(boxaile, text="The value has been inserted")
        myLabel.grid(row=4,column=0)

    def insert(self, database, val1, val2, val3):
        name=val1.get()
        price=val2.get()
        date=val3.get()
        insertion=database(name, price, date)
        return insertion
    
    def groceries(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_title = Label(self.frame, text='Groceries expenses', font=('Arial', 14, 'bold'))
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        label_name = Label(self.frame, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        label_price = Label(self.frame, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        label_date = Label(self.frame, text="Date of pruchase").grid(row=3, column=0, sticky=W, pady=2)

        entry_name = Entry(self.frame).grid(row=1, column=1, sticky=W, pady=2)
        entry_price = Entry(self.frame).grid(row=2, column=1, sticky=W, pady=2)
        entry_date = Entry(self.frame).grid(row=3, column=1, sticky=W, pady=2)

def main():
    root = Tk()
    root.geometry('250x200')
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)

    #Menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    type_menu = Menu(menubar, tearoff=False)
    type_menu.add_command(label='Groceries expenses', command=tracker.groceries)
    type_menu.add_command(label="Transportation expenses", command=tracker.transportation)
    type_menu.add_command(label="Entertainment expenses")
    type_menu.add_command(label="Utilities expenses")
    type_menu.add_command(label="Other expenses")

    exit_menu = Menu(menubar, tearoff=0)
    exit_menu.add_command(label='Exit', command=root.destroy)

    menubar.add_cascade(label="Types", menu=type_menu)
    menubar.add_cascade(label="Other", menu=exit_menu)
    

    root.mainloop()

main()
