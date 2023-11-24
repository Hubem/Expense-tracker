from Adatbazis import db
from tkinter import *
from tkinter.ttk import *

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()


    def display_all(self,database):
        select_all = database
        return select_all

    def delete(self, boxaile):
        myLabel=Label(boxaile, text="The chosen value was successfully deleted")
        myLabel.grid(row=4,column=0)

    def delete_expense(self, database,val1, val2):
        name=val1.get()
        price=val2.get()
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
    
    def show_expenses(self,select_all_func):
        expenses = select_all_func()
        expense_list = Listbox(self.frame,selectmode=SINGLE)
        scroll_bar = Scrollbar(self.frame,orient='vertical',command=expense_list.yview)
        expense_list.config(yscrollcommand=scroll_bar.set)

        for expense in expenses:
            expense_list.insert(END,f"{expense[0]} - {expense[1]} - {expense[2]}")
        
        expense_list.grid(row=4,column=0,columnspan=2)
        scroll_bar.grid(row=4,column=2)

        delete_button = Button(self.frame,text='Delete the Selected',command= lambda: self.delete_selected(database,expense_list))
        delete_button.grid(row=5,column=0,columnspan=2  )

    def groceries(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_title = Label(self.frame, text='Groceries expenses', font=('Arial', 14, 'bold'))
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        label_name = Label(self.frame, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        label_price = Label(self.frame, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        label_date = Label(self.frame, text="Date of pruchase").grid(row=3, column=0, sticky=W, pady=2)

        entry_name = Entry(self.frame)
        entry_name.grid(row=1, column=1, sticky=W, pady=2)
        entry_price = Entry(self.frame)
        entry_price.grid(row=2, column=1, sticky=W, pady=2)
        entry_date = Entry(self.frame)
        entry_date.grid(row=3, column=1, sticky=W, pady=2)

        ButtonInsert = Button(self.frame,text="Insert values",command= lambda: (self.insert(db.insert_groceries,entry_name,entry_price,entry_date),self.inserted(self.frame)))
        ButtonInsert.grid(row=1,column=2)

        ButtonDelete = Button(self.frame,text="Delete Groceries",command= lambda: (self.show_expenses(db.select_all_groceries),self.delete(self.frame)))
        ButtonDelete.grid(row=2,column=2)


    def transportation(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_title = Label(self.frame, text='Transportation expenses', font=('Arial', 14, 'bold'))
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        label_name = Label(self.frame, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        label_price = Label(self.frame, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        label_date = Label(self.frame, text="Date of pruchase").grid(row=3, column=0, sticky=W, pady=2)

        entry_name = Entry(self.frame)
        entry_name.grid(row=1, column=1, sticky=W, pady=2)
        entry_price = Entry(self.frame)
        entry_price.grid(row=2, column=1, sticky=W, pady=2)
        entry_date = Entry(self.frame)
        entry_date.grid(row=3, column=1, sticky=W, pady=2)

        ButtonInsert = Button(self.frame,text="Insert values",command= lambda: (self.insert(db.insert_transportation,entry_name,entry_price,entry_date),self.inserted(self.frame)))
        ButtonInsert.grid(row=1,column=2)
        

def main():
    root = Tk()
    root.geometry('800x500')
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)
    db.create_tables()

    #Menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    type_menu = Menu(menubar, tearoff=False)
    type_menu.add_command(label='Groceries expenses', command=tracker.groceries)
    type_menu.add_command(label='Transportation expenses', command=tracker.transportation)
    type_menu.add_command(label="Entertainment expenses")
    type_menu.add_command(label="Utilities expenses")
    type_menu.add_command(label="Other expenses")

    exit_menu = Menu(menubar, tearoff=0)
    exit_menu.add_command(label='Exit', command=root.destroy)

    menubar.add_cascade(label="Types", menu=type_menu)
    menubar.add_cascade(label="Other", menu=exit_menu)
    

    root.mainloop()

main()
