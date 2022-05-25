from controller.AccountController import AccountController
from view.AccountTableView import AccountTableView
from view.AccountInfoView import AccountInfoView
import tkinter as tk


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

        self.left_panel.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)
        self.right_panel.pack(fill=tk.BOTH, side=tk.RIGHT, expand=1)

        # setup menubar
        self.menubar = tk.Menu(self.container)
        account_menu = tk.Menu(self.menubar, tearoff=0)
        account_menu.add_command(label='Add Account', command=self.add_account)
        account_menu.add_command(label='Refresh', command=self.refresh_accounts)
        account_menu.add_separator()
        account_menu.add_command(label='Exit', command=self.container.quit)
        self.menubar.add_cascade(label='Accounts', menu=account_menu)

        self.container.config(menu=self.menubar)

    def add_account(self):
        print('adding new account...')

    def refresh_accounts(self):
        self.left_panel.refresh_table()
