from textwrap import fill
from turtle import right
from Adatbazis import db
from tkinter import *
from tkinter.ttk import *
import customtkinter
import re
import matplotlib.pyplot as plt
import numpy

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.tracker = self

    def center_button(self, text, command,image,compound):
        button = customtkinter.CTkButton(self.frame, text=text, command=command,border_width=2,image=image,compound=compound,bg_color='transparent',corner_radius=8)
        
        button.pack(side='left')
        


    def display_all(self,database):
        select_all = database
        return select_all

    def delete_expense(self, database,name, price):
        delete = database(name, price)
        return delete
    
    
    def inserted(self, boxaile):
        myLabel=Label(boxaile, text="The value has been inserted")
        myLabel.grid(row=4,column=0)
        myLabel.after(1200,myLabel.destroy)
    
    def price_error(self, boxaile):
        priceLabel=Label(boxaile, text="Error: The price should be a number!")
        priceLabel.grid(row=5,column=0)
        priceLabel.after(4000,priceLabel.destroy)
    
    def date_error(self, boxaile):
        dateLabel=Label(boxaile, text="Error: The date has an incorrect format. Use this: yyyy.mm.dd")
        dateLabel.grid(row=5,column=0)
        dateLabel.after(5000,dateLabel.destroy)

    def insert(self, database, entry_name, entry_price, entry_date):
        name = entry_name.get()
        price = entry_price.get()
        date = entry_date.get()
        insertion = database(name, price, date)
        return insertion
    
    def price_constraint(self, price):
        try:
            int(price.get())
            return True
        except ValueError:
            self.price_error(self.frame)
            return False

    def date_constraint(self, date):
        date_pattern = re.compile("^\d{4}\.\d{2}\.\d{2}$")
        if date_pattern.match(date.get()):
            return True
        self.date_error(self.frame)
        return False
    
    def check_both_constraint(self, price, date):
        if(not self.price_constraint(price)):
            return False
        if(not self.date_constraint(date)):
            return False
        return True

    def show_expenses_g(self,database):   
        expenses = database()
        self.expense_list = Listbox(self.frame,selectmode=SINGLE)
        scroll_bar = Scrollbar(self.frame,orient='vertical',command=self.expense_list.yview)
        self.expense_list.config(yscrollcommand=scroll_bar.set)

        for expense in expenses:
            self.expense_list.insert(END,f"{expense[0]} - {expense[1]} - {expense[2]}")

        self.expense_list.grid(row=4,column=0,columnspan=2)
        scroll_bar.grid(row=4,column=2)

        delete_button = customtkinter.CTkButton(self.frame,text='Delete the Selected',command= lambda: self.delete_selected_g(database,self.expense_list))
        delete_button.grid(row=5,column=0,columnspan=2)

    def show_expenses_gnd(self,database):
        expenses = database()
        self.expense_list = Listbox(self.frame,selectmode=SINGLE)
        scroll_bar = Scrollbar(self.frame,orient='vertical',command=self.expense_list.yview)
        self.expense_list.config(yscrollcommand=scroll_bar.set)

        for expense in expenses:
            self.expense_list.insert(END,f"{expense[0]} - {expense[1]} - {expense[2]}")

        self.expense_list.grid(row=4,column=0,columnspan=2)
        scroll_bar.grid(row=4,column=2)

        self.expense_list.after(3000,self.expense_list.destroy)
        scroll_bar.after(3000,scroll_bar.destroy)
    
    
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

        delete_button = customtkinter.CTkButton(self.frame,text='Delete the Selected',command= lambda: self.delete_selected_t(database,self.expense_list))
        delete_button.grid(row=5,column=0,columnspan=2)

    def delete_selected_t(self,database,expense_list):
            selected = expense_list.curselection()

            if selected:
                id_to_delete = int(expense_list.get(selected[0]).split()[0])
                db.delete_transp_by_id(id_to_delete)
            self.show_expenses_t(database)
        
    def show_expenses_e(self,database):   
            expenses = database()
            self.expense_list = Listbox(self.frame,selectmode=SINGLE)
            scroll_bar = Scrollbar(self.frame,orient='vertical',command=self.expense_list.yview)
            self.expense_list.config(yscrollcommand=scroll_bar.set)

            for expense in expenses:
                self.expense_list.insert(END,f"{expense[0]} - {expense[1]} - {expense[2]}")

            self.expense_list.grid(row=4,column=0,columnspan=2)
            scroll_bar.grid(row=4,column=2)

            delete_button = Button(self.frame,text='Delete the Selected',command= lambda: self.delete_selected_e(database,self.expense_list))
            delete_button.grid(row=5,column=0,columnspan=2)

    def delete_selected_e(self,database,expense_list):
            selected = expense_list.curselection()

            if selected:
                id_to_delete = int(expense_list.get(selected[0]).split()[0])
                db.delete_ent_by_id(id_to_delete)
            self.show_expenses_e(database)    


    def show_expenses_o(self,database):   
        expenses = database()
        self.expense_list = Listbox(self.frame,selectmode=SINGLE)
        scroll_bar = Scrollbar(self.frame,orient='vertical',command=self.expense_list.yview)
        self.expense_list.config(yscrollcommand=scroll_bar.set)

        for expense in expenses:
            self.expense_list.insert(END,f"{expense[0]} - {expense[1]} - {expense[2]}")

        self.expense_list.grid(row=4,column=0,columnspan=2)
        scroll_bar.grid(row=4,column=2)

        delete_button = customtkinter.CTkButton(self.frame,text='Delete the Selected',command= lambda: self.delete_selected_o(database,self.expense_list))
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

        delete_button = customtkinter.CTkButton(self.frame,text='Delete the Selected',command= lambda: self.delete_selected_u(database,self.expense_list))
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

        entry_name = customtkinter.CTkEntry(self.frame)
        entry_name.grid(row=1, column=1, sticky=W, pady=2)
        entry_price = customtkinter.CTkEntry(self.frame)
        entry_price.grid(row=2, column=1, sticky=W, pady=2)
        entry_date = customtkinter.CTkEntry(self.frame)
        entry_date.grid(row=3, column=1, sticky=W, pady=2)

        ButtonInsert = customtkinter.CTkButton(self.frame,text="Insert values",command= lambda: ((self.insert(db.insert_groceries,entry_name,entry_price,entry_date),self.inserted(self.frame)) if self.check_both_constraint(entry_price, entry_date) else 1))
        ButtonInsert.grid(row=1,column=2)

        ButtonDelete = customtkinter.CTkButton(self.frame, text="Delete Groceries", command=lambda: (self.show_expenses_g(db.select_all_gro)))
        ButtonDelete.grid(row=2, column=2)

        ButtonBack = customtkinter.CTkButton(self.frame,text='Back',command=lambda: self.show_main())
        ButtonBack.grid(row=3,column=2)

        ButtonAll = customtkinter.CTkButton(self.frame,text='Show all',command=lambda:self.show_expenses_gnd(db.select_all_gro))
        ButtonAll.grid(row=2,column=3)

    def transportation(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_title = Label(self.frame, text='Transportation expenses', font=('Arial', 14, 'bold'))
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        label_name = Label(self.frame, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        label_price = Label(self.frame, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        label_date = Label(self.frame, text="Date of pruchase").grid(row=3, column=0, sticky=W, pady=2)

        entry_name = customtkinter.CTkEntry(self.frame)
        entry_name.grid(row=1, column=1, sticky=W, pady=2)
        entry_price = customtkinter.CTkEntry(self.frame)
        entry_price.grid(row=2, column=1, sticky=W, pady=2)
        entry_date = customtkinter.CTkEntry(self.frame)
        entry_date.grid(row=3, column=1, sticky=W, pady=2)

        ButtonInsert = customtkinter.CTkButton(self.frame,text="Insert values",command= lambda: ((self.insert(db.insert_transportation,entry_name,entry_price,entry_date),self.inserted(self.frame)) if self.check_both_constraint(entry_price, entry_date) else 1))
        ButtonInsert.grid(row=1,column=2)

        ButtonDelete = customtkinter.CTkButton(self.frame, text="Delete Transportation", command=lambda: (self.show_expenses_t(db.select_all_transp)))
        ButtonDelete.grid(row=2, column=2)

        ButtonBack = customtkinter.CTkButton(self.frame,text='Back',command=lambda: self.show_main())
        ButtonBack.grid(row=3,column=2)

    def entertainment(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_title = Label(self.frame, text='Entertainment expenses', font=('Arial', 14, 'bold'))
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        label_name = Label(self.frame, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        label_price = Label(self.frame, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        label_date = Label(self.frame, text="Date of pruchase").grid(row=3, column=0, sticky=W, pady=2)

        entry_name = customtkinter.CTkEntry(self.frame)
        entry_name.grid(row=1, column=1, sticky=W, pady=2)
        entry_price = customtkinter.CTkEntry(self.frame)
        entry_price.grid(row=2, column=1, sticky=W, pady=2)
        entry_date = customtkinter.CTkEntry(self.frame)
        entry_date.grid(row=3, column=1, sticky=W, pady=2)

        ButtonInsert = customtkinter.CTkButton(self.frame,text="Insert values",command= lambda: ((self.insert(db.insert_entertainment,entry_name,entry_price,entry_date),self.inserted(self.frame)) if self.check_both_constraint(entry_price, entry_date) else 1))
        ButtonInsert.grid(row=1,column=2)

        ButtonDelete = customtkinter.CTkButton(self.frame, text="Delete Entertainment", command=lambda: (self.show_expenses_e(db.select_all_ent)))
        ButtonDelete.grid(row=2, column=2)


        ButtonBack = customtkinter.CTkButton(self.frame,text='Back',command=lambda: self.show_main())
        ButtonBack.grid(row=3,column=2)
    def utilities(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_title = Label(self.frame, text="Utilities", font=('Arial', 14, 'bold'))
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        label_name = Label(self.frame, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        label_price = Label(self.frame, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        label_date = Label(self.frame, text="Date of pruchase").grid(row=3, column=0, sticky=W, pady=2)

        entry_name = customtkinter.CTkEntry(self.frame)
        entry_name.grid(row=1, column=1, sticky=W, pady=2)
        entry_price = customtkinter.CTkEntry(self.frame)
        entry_price.grid(row=2, column=1, sticky=W, pady=2)
        entry_date = customtkinter.CTkEntry(self.frame)
        entry_date.grid(row=3, column=1, sticky=W, pady=2)

        ButtonInsert = customtkinter.CTkButton(self.frame,text="Insert values",command= lambda: ((self.insert(db.insert_utilities,entry_name,entry_price,entry_date),self.inserted(self.frame)) if self.check_both_constraint(entry_price, entry_date) else 1))
        ButtonInsert.grid(row=1,column=2)

        ButtonDelete = customtkinter.CTkButton(self.frame, text="Delete Utilities", command=lambda: (self.show_expenses_u(db.select_all_uti)))
        ButtonDelete.grid(row=2, column=2)

        ButtonBack = customtkinter.CTkButton(self.frame,text='Back',command=lambda: self.show_main())
        ButtonBack.grid(row=3,column=2)

        
    def other(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        label_title = Label(self.frame, text='Other expenses', font=('Arial', 14, 'bold'))
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        label_name = Label(self.frame, text="Name of good").grid(row=1, column=0, sticky=W, pady=2)
        label_price = Label(self.frame, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        label_date = Label(self.frame, text="Date of pruchase").grid(row=3, column=0, sticky=W, pady=2)

        entry_name = customtkinter.CTkEntry(self.frame)
        entry_name.grid(row=1, column=1, sticky=W, pady=2)
        entry_price = customtkinter.CTkEntry(self.frame)
        entry_price.grid(row=2, column=1, sticky=W, pady=2)
        entry_date = customtkinter.CTkEntry(self.frame)
        entry_date.grid(row=3, column=1, sticky=W, pady=2)

        ButtonInsert = customtkinter.CTkButton(self.frame,text="Insert values",command= lambda: ((self.insert(db.insert_other,entry_name,entry_price,entry_date),self.inserted(self.frame)) if self.check_both_constraint(entry_price, entry_date) else 1))
        ButtonInsert.grid(row=1,column=2)

        ButtonDelete = customtkinter.CTkButton(self.frame, text="Delete Other", command=lambda: (self.show_expenses_o(db.select_all_oth)))
        ButtonDelete.grid(row=2, column=2)

        ButtonBack = customtkinter.CTkButton(self.frame,text='Back',command=lambda: self.show_main())
        ButtonBack.grid(row=3,column=2)

    def show_graph(self, cat, start, end):
        if not (self.date_constraint(start) or self.date_constraint(end)):
            return
        if cat == "Groceries":
            dates = []
            prices = []
            output = db.groceries_date(start.get(), end.get())
            lines = output.split("\n")[:-1]
            for line in lines:
                split_line = line.split()
                prices.append(split_line[1])
                dates.append(split_line[2])
            hist = {}
            for date, price in zip(dates, prices):
                hist[date] = hist.get(date, 0) + int(price)
            fig, ax = plt.subplots()
            ax.bar(hist.keys(), hist.values())
            ax.set_title(f"Groceries expenses from {start.get()} to {end.get()}")
            fig.show()
            
        elif cat == "Transportation":
            dates = []
            prices = []
            output = db.transportation_date(start.get(), end.get())
            lines = output.split("\n")[:-1]
            for line in lines:
                print(line.split())
                split_line = line.split()
                prices.append(split_line[1])
                dates.append(split_line[2])
            hist = {}
            for date, price in zip(dates, prices):
                hist[date] = hist.get(date, 0) + int(price)
            fig, ax = plt.subplots()
            ax.bar(hist.keys(), hist.values())
            ax.set_title(f"Transportation expenses from {start.get()} to {end.get()}")
            fig.show()
        elif cat == "Entertainment":
            dates = []
            prices = []
            output = db.entertainment_date(start.get(), end.get())
            lines = output.split("\n")[:-1]
            for line in lines:
                print(line.split())
                split_line = line.split()
                prices.append(split_line[1])
                dates.append(split_line[2])
            hist = {}
            for date, price in zip(dates, prices):
                hist[date] = hist.get(date, 0) + int(price)
            fig, ax = plt.subplots()
            ax.bar(hist.keys(), hist.values())
            ax.set_title(f"Entertainment expenses from {start.get()} to {end.get()}")
            fig.show()
        elif cat == "Utilities":
            dates = []
            prices = []
            output = db.utilities_date(start.get(), end.get())
            lines = output.split("\n")[:-1]
            for line in lines:
                print(line.split())
                split_line = line.split()
                prices.append(split_line[1])
                dates.append(split_line[2])
            hist = {}
            for date, price in zip(dates, prices):
                hist[date] = hist.get(date, 0) + int(price)
            fig, ax = plt.subplots()
            ax.bar(hist.keys(), hist.values())
            ax.set_title(f"Utilities expenses from {start.get()} to {end.get()}")
            fig.show()
        elif cat == "Other":
            dates = []
            prices = []
            output = db.other_date(start.get(), end.get())
            lines = output.split("\n")[:-1]
            for line in lines:
                print(line.split())
                split_line = line.split()
                prices.append(split_line[1])
                dates.append(split_line[2])
            hist = {}
            for date, price in zip(dates, prices):
                hist[date] = hist.get(date, 0) + int(price)
            fig, ax = plt.subplots()
            ax.set_title(f"Other expenses from {start.get()} to {end.get()}")
            ax.bar(hist.keys(), hist.values())
            fig.show()
    def graph(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        label_title = Label(self.frame, text='Show graph', font=('Arial', 14, 'bold'))
        label_title.grid(row=0, column=0, columnspan=2, pady=10)
        
        label_combobox = Label(self.frame, text="Category:").grid(row=1, column=0, sticky=W, pady=2)
        label_startdate = Label(self.frame, text="From").grid(row=2, column=0, sticky=W, pady=2)
        label_enddate = Label(self.frame, text="To").grid(row=3, column=0, sticky=W, pady=2)
        
        category_combobox = Combobox(self.frame, values=["Groceries", "Transportation", "Entertainment", "Utilities", "Other"])
        category_combobox.grid(row=1, column=1, sticky=W, pady=2)
        entry_start = customtkinter.CTkEntry(self.frame)
        entry_start.grid(row=2, column=1, sticky=W, pady=2)
        entry_end = customtkinter.CTkEntry(self.frame)
        entry_end.grid(row=3, column=1, sticky=W, pady=2)
        
        ButtonShow = customtkinter.CTkButton(self.frame, text="Show", command=lambda: self.show_graph(category_combobox.get(), entry_start, entry_end))
        ButtonShow.grid(row=2, column=2)

        ButtonBack = customtkinter.CTkButton(self.frame,text='Back',command=lambda: self.show_main())
        ButtonBack.grid(row=3,column=2)

    def show_main(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.display_main()

    def display_main(self):
        minecart = PhotoImage(file="images/pngegg.png")
        firewok = PhotoImage(file="images/firework.png")
        bread = PhotoImage(file="images/bread.png")
        armor = PhotoImage(file='images/armor.png')
        door = PhotoImage(file='images/door.png')
        width = 22
        height = 22
        resizedMine = minecart.subsample(int(minecart.width()/width),int(minecart.height()/height))
        resizedFire = firewok.subsample(int(firewok.width()/width),int(firewok.height()/height))
        resizedBread = bread.subsample(int(bread.width()/width),int(bread.height()/height))
        resizedArmor = armor.subsample(int(armor.width()/width),int(armor.height()/height))
        resizedDoor = door.subsample(int(door.width()/width),int(door.height()/height))

        self.center_button('Groceries expenses',self.groceries,image=resizedBread,compound="left")
        self.center_button('Transportation expenses',self.transportation,image=resizedMine,compound="left")
        self.center_button("Entertainment expenses",self.entertainment, image=resizedFire,compound="left")
        self.center_button("Utilities expenses",self.utilities,image=resizedArmor,compound="left")
        self.center_button("Other expenses",self.other,image=resizedMine,compound="left")
        self.center_button("Show graph", self.graph, image=resizedBread, compound="left")
        self.center_button('Exit',root.destroy,image=resizedDoor,compound='left')
        
    
def main():
    global root
    root = customtkinter.CTk()
    root.geometry('1150x800')
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)
    db.create_tables()
    #customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('blue')


    minecart = PhotoImage(file="images/pngegg.png")
    firewok = PhotoImage(file="images/firework.png")
    bread = PhotoImage(file="images/bread.png")
    armor = PhotoImage(file='images/armor.png')
    door = PhotoImage(file='images/door.png')
    width = 22
    height = 22
    resizedMine = minecart.subsample(int(minecart.width()/width),int(minecart.height()/height))
    resizedFire = firewok.subsample(int(firewok.width()/width),int(firewok.height()/height))
    resizedBread = bread.subsample(int(bread.width()/width),int(bread.height()/height))
    resizedArmor = armor.subsample(int(armor.width()/width),int(armor.height()/height))
    resizedDoor = door.subsample(int(door.width()/width),int(door.height()/height))




    tracker.center_button('Groceries expenses',tracker.groceries,image=resizedBread,compound="left")
    tracker.center_button('Transportation expenses',tracker.transportation,image=resizedMine,compound="left")
    tracker.center_button("Entertainment expenses",tracker.entertainment, image=resizedFire,compound="left")
    tracker.center_button("Utilities expenses",tracker.utilities,image=resizedArmor,compound="left")
    tracker.center_button("Other expenses",tracker.other,image=resizedFire,compound="left")
    tracker.center_button("Show graph", tracker.graph,image=resizedBread, compound="left")
    tracker.center_button('Exit',root.destroy,image=resizedDoor,compound='left')

    

    root.mainloop()

main()
