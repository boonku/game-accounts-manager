from tkinter import ttk
import tkinter as tk


class AccountInfoView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.account_info_field: tk.Text = None
        self.__setup()

    def __setup(self):
        account_lbl = tk.Label(self, text='Account Info')
        account_lbl.pack(side=tk.TOP, fill=tk.BOTH)
        self.account_info_field = tk.Text(self)
        self.account_info_field.pack(fill=tk.BOTH, expand=1)

    def set_account_info(self, account):
        if len(self.account_info_field.get(1.0, tk.END)):
            self.account_info_field.delete(1.0, tk.END)
        # print json for now, will be changed later
        self.account_info_field.insert(tk.END, account.to_json())
        self.account_info_field.insert(tk.END, f'\n\n\ndecoded_password: {self.controller.decode_password(account)}')
