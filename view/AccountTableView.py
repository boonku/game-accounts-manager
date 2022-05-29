import tkinter as tk
from tkinter import ttk


class AccountTableView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.accounts_list_table: ttk.Treeview = None
        self.__setup()

    def __setup(self):
        self.display_accounts()
        self.accounts_list_table.bind('<<TreeviewSelect>>', self.account_select)

    def display_accounts(self):
        columns = ('acc_id', 'game', 'platform')
        columns_name = ('', 'Game', 'Platform')
        self.accounts_list_table = ttk.Treeview(self, columns=columns, show='headings')
        for col, col_name in zip(columns, columns_name):
            self.accounts_list_table.heading(col, text=col_name)
        # don't show id's in the table, but store them for database searches
        self.accounts_list_table['displaycolumns'] = ('game', 'platform')
        self.insert_all()
        # add scrollbar to table
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.accounts_list_table.yview)
        scrollbar.pack(side='right', fill='y')
        self.accounts_list_table.configure(yscrollcommand=scrollbar.set)
        self.accounts_list_table.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)

    def refresh_table(self):
        self.controller.clear()

    def account_select(self, event):
        for selected_account in self.accounts_list_table.selection():
            account = self.accounts_list_table.item(selected_account)
            record = account['values']
            self.controller.set_account_info(record[0])

    def clear_all(self):
        for item in self.accounts_list_table.get_children():
            self.accounts_list_table.delete(item)

    def insert_all(self):
        for account in self.controller.get_accounts():
            self.accounts_list_table.insert('', tk.END,
                                            values=(account.id, account.game.name, account.platform.name))
