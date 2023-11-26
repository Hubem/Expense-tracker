import unittest
import datetime
from unittest.mock import patch
from Adatbazis import db
from tkinter import *
from tkinter.ttk import *
from main import ExpenseTracker


import unittest
from unittest.mock import MagicMock

from Adatbazis import db  

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        # Create a mock database for testing
        self.mock_db = MagicMock()
        self.tracker = ExpenseTracker(self.mock_db)

    def test_insert(self):
        entry_name = MagicMock()
        entry_price = MagicMock()
        entry_date = MagicMock()

        # Call the insert method
        self.tracker.insert(self.mock_db, entry_name, entry_price, entry_date)

        # Check that the insert method of the mock database was called
        self.mock_db.assert_called_once_with(entry_name.get(), entry_price.get(), entry_date.get())

    def test_show_expenses(self):
        # Call the show_expenses method
        self.tracker.show_expenses(self.mock_db)

        # Check that the Listbox was created
        self.assertIsInstance(self.tracker.expense_list, Listbox)


    def test_delete_groceries(self):
        # Insert value
        entry_name = Entry(self.tracker.frame)  # Create a mock Entry widget for testing
        entry_name.insert(0, 'Sample_Grocery')  # Set the value in the mock Entry widget
        entry_price = Entry(self.tracker.frame)
        entry_price.insert(0, 10)
        entry_date = Entry(self.tracker.frame)
        entry_date.insert(0, '2023-01-01')

        # Call insert with the mock Entry widgets
        self.tracker.insert(self.mock_db.insert_groceries, entry_name, entry_price, entry_date)

        # Call delete_groceries
        self.tracker.delete_expense(self.mock_db,entry_name.get(), entry_price.get())

        # Check if the value is no longer present in the database
        expenses_after_delete = self.mock_db.show_expenses(self.mock_db)
        self.assertNotIn('Sample_Grocery - 10 - 2023-01-01', expenses_after_delete)


    def test_delete_selected_no_selection(self):
       
     mock_listbox = MagicMock()
     mock_listbox.curselection.return_value = ()
     self.tracker.expense_list = mock_listbox
    
     self.tracker.delete_selected(self.mock_db, mock_listbox)
     
     self.mock_db.delete_gro_by_id.assert_not_called()

if __name__ == '__main__':
    unittest.main()