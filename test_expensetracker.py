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

    def test_delete_selected_no_selection(self):
       
     mock_listbox = MagicMock()
     mock_listbox.curselection.return_value = ()
     self.tracker.expense_list = mock_listbox
    
     self.tracker.delete_selected(self.mock_db, mock_listbox)
     
     self.mock_db.delete_gro_by_id.assert_not_called()

if __name__ == '__main__':
    unittest.main()