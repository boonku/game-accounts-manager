import tkinter as tk
from tkinter.messagebox import showerror

from controller.AccountController import AccountController
from view.AccountInfoView import AccountInfoView
from view.AccountTableView import AccountTableView
from view.AddAccountView import AddAccountView
from view.ExportAccountView import ExportAccountView
from view.ImportAccountView import ImportAccountExportImport


class MainView:
    def __init__(self, parent):
        self.container = parent
        self.controller = AccountController()
        self.left_panel: AccountTableView = None
        self.right_panel: AccountInfoView = None
        self.menubar: tk.Menu = None
        self.__setup()

    def __setup(self):
        self.left_panel = AccountTableView(self.container, self.controller)
        self.right_panel = AccountInfoView(self.container, self.controller)

        self.controller.accounts_table_view = self.left_panel
        self.controller.account_info_view = self.right_panel

        self.left_panel.pack(fill=tk.BOTH, side=tk.LEFT, expand=1, padx=10, pady=10)
        self.right_panel.pack(fill=tk.BOTH, side=tk.RIGHT, expand=1, padx=10, pady=10)

        # setup menubar
        self.menubar = tk.Menu(self.container)
        account_menu = tk.Menu(self.menubar, tearoff=0)
        account_menu.add_command(label='Add Account', command=self.add_account)
        account_menu.add_command(label='Refresh', command=self.refresh_accounts)
        account_menu.add_separator()
        account_menu.add_command(label='Export Account', command=self.export_account)
        account_menu.add_command(label='Import Account', command=self.import_account)
        account_menu.add_separator()
        account_menu.add_command(label='Exit', command=self.container.quit)
        self.menubar.add_cascade(label='Accounts', menu=account_menu)

        self.container.config(menu=self.menubar)

    def add_account(self):
        AddAccountView(self.container, self.controller)

    def refresh_accounts(self):
        self.left_panel.refresh_table()

    def export_account(self):
        viewed_account_id = self.right_panel.viewed_account_id
        if viewed_account_id:
            ExportAccountView(self.container, self.controller, viewed_account_id)
        else:
            showerror(title='Error', message='No account selected to export')

    def import_account(self):
        ImportAccountExportImport(self.container, self.controller)
