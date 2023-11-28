from Adatbazis import db
from tkinter import *
from tkinter.ttk import *

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.tracker = self


    def display_all(self,database):
        select_all = database
        return select_all

    def delete(self, boxaile):
        myLabel=Label(boxaile, text="The chosen value was successfully deleted")
        myLabel.grid(row=4,column=0)

    def delete_expense(self, database,name, price):
        delete = database(name, price)
        return delete
    
    
    def inserted(self, boxaile):
        myLabel=Label(boxaile, text="The value has been inserted")
        myLabel.grid(row=4,column=0)

    def insert(self, database, entry_name, entry_price, entry_date):
        name = entry_name.get()
        price = entry_price.get()
        date = entry_date.get()
        insertion = database(name, price, date)
        return insertion
    


    def show_expenses_g(self,database):   
        expenses = database()
        self.expense_list = Listbox(self.frame,selectmode=SINGLE)
        scroll_bar = Scrollbar(self.frame,orient='vertical',command=self.expense_list.yview)
        self.expense_list.config(yscrollcommand=scroll_bar.set)

        for expense in expenses:
            self.expense_list.insert(END,f"{expense[0]} - {expense[1]} - {expense[2]}")

        self.expense_list.grid(row=4,column=0,columnspan=2)
        scroll_bar.grid(row=4,column=2)

        delete_button = Button(self.frame,text='Delete the Selected',command= lambda: self.delete_selected_g(database,self.expense_list))
        delete_button.grid(row=5,column=0,columnspan=2)
    
    
    def delete_selected_g(self,database,expense_list):
        selected = expense_list.curselection()

        if selected:
            id_to_delete = int(expense_list.get(selected[0]).split()[0])
            db.delete_gro_by_id(id_to_delete)
        self.show_expenses_g(database)



    def show_expenses_t(self,database):   
        expenses = database()
        self.expense_list = Listbox(self.frame,selectmode=SINGLE)
        scroll_bar = Scrollbar(self.frame,orient='vertical',command=self.expense_list.yview)
        self.expense_list.config(yscrollcommand=scroll_bar.set)

        for expense in expenses:
            self.expense_list.insert(END,f"{expense[0]} - {expense[1]} - {expense[2]}")

        self.expense_list.grid(row=4,column=0,columnspan=2)
        scroll_bar.grid(row=4,column=2)

        delete_button = Button(self.frame,text='Delete the Selected',command= lambda: self.delete_selected_t(database,self.expense_list))
        delete_button.grid(row=5,column=0,columnspan=2)

    def delete_selected_t(self,database,expense_list):
            selected = expense_list.curselection()

            if selected:
                id_to_delete = int(expense_list.get(selected[0]).split()[0])
                db.delete_transp_by_id(id_to_delete)
            self.show_expenses_t(database)
        


    def show_expenses_o(self,database):   
        expenses = database()
        self.expense_list = Listbox(self.frame,selectmode=SINGLE)
        scroll_bar = Scrollbar(self.frame,orient='vertical',command=self.expense_list.yview)
        self.expense_list.config(yscrollcommand=scroll_bar.set)

        for expense in expenses:
            self.expense_list.insert(END,f"{expense[0]} - {expense[1]} - {expense[2]}")

        self.expense_list.grid(row=4,column=0,columnspan=2)
        scroll_bar.grid(row=4,column=2)

        delete_button = Button(self.frame,text='Delete the Selected',command= lambda: self.delete_selected_o(database,self.expense_list))
        delete_button.grid(row=5,column=0,columnspan=2)

    def delete_selected_o(self,database,expense_list):
            selected = expense_list.curselection()

            if selected:
                id_to_delete = int(expense_list.get(selected[0]).split()[0])
                db.delete_other_by_id(id_to_delete)
            self.show_expenses_o(database)



    def show_expenses_u(self,database):   
        expenses = database()
        self.expense_list = Listbox(self.frame,selectmode=SINGLE)
        scroll_bar = Scrollbar(self.frame,orient='vertical',command=self.expense_list.yview)
        self.expense_list.config(yscrollcommand=scroll_bar.set)

        for expense in expenses:
            self.expense_list.insert(END,f"{expense[0]} - {expense[1]} - {expense[2]}")

        self.expense_list.grid(row=4,column=0,columnspan=2)
        scroll_bar.grid(row=4,column=2)

        delete_button = Button(self.frame,text='Delete the Selected',command= lambda: self.delete_selected_u(database,self.expense_list))
        delete_button.grid(row=5,column=0,columnspan=2)

    def delete_selected_u(self,database,expense_list):
            selected = expense_list.curselection()

            if selected:
                id_to_delete = int(expense_list.get(selected[0]).split()[0])
                db.delete_uti_by_id(id_to_delete)
            self.show_expenses_u(database)



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

        ButtonDelete = Button(self.frame, text="Delete Groceries", command=lambda: (self.show_expenses_g(db.select_all_gro)))
        ButtonDelete.grid(row=2, column=2)

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

        ButtonDelete = Button(self.frame, text="Delete Transportation", command=lambda: (self.show_expenses_t(db.select_all_transp)))
        ButtonDelete.grid(row=2, column=2)



    def utilities(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_title = Label(self.frame, text="Utilities", font=('Arial', 14, 'bold'))
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

        ButtonInsert = Button(self.frame,text="Insert values",command= lambda: (self.insert(db.insert_utilities,entry_name,entry_price,entry_date),self.inserted(self.frame)))
        ButtonInsert.grid(row=1,column=2)

        ButtonDelete = Button(self.frame, text="Delete Utilities", command=lambda: (self.show_expenses_u(db.select_all_uti)))
        ButtonDelete.grid(row=2, column=2)

        
    def other(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_title = Label(self.frame, text='Other expenses', font=('Arial', 14, 'bold'))
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

        ButtonInsert = Button(self.frame,text="Insert values",command= lambda: (self.insert(db.insert_other,entry_name,entry_price,entry_date),self.inserted(self.frame)))
        ButtonInsert.grid(row=1,column=2)

        ButtonDelete = Button(self.frame, text="Delete Other", command=lambda: (self.show_expenses_o(db.select_all_oth)))
        ButtonDelete.grid(row=2, column=2)
        

def main():
    root = Tk()
    root.geometry('1000x800')
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)
    db.create_tables()

    #Menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    minecart = PhotoImage(file="images/pngegg.png")
    firewok = PhotoImage(file="images/firework.png")
    width = 12
    height = 12
    resizedMine = minecart.subsample(int(minecart.width()/width),int(minecart.height()/height))
    resizedFire = minecart.subsample(int(firewok.width()/width),int(firewok.height()/height))

    type_menu = Menu(menubar, tearoff=False)
    type_menu.add_command(label='Groceries expenses', command=tracker.groceries)
    type_menu.add_command(label='Transportation expenses', command=tracker.transportation,image=resizedMine,compound="left")
    type_menu.add_command(label="Entertainment expenses",image=resizedFire,compound="left")
    type_menu.add_command(label="Utilities expenses", command=tracker.utilities)
    type_menu.add_command(label="Other expenses", command=tracker.other)

    exit_menu = Menu(menubar, tearoff=0)
    exit_menu.add_command(label='Exit', command=root.destroy)

    menubar.add_cascade(label="Types", menu=type_menu)
    menubar.add_cascade(label="Other", menu=exit_menu)
    

    root.mainloop()

main()
