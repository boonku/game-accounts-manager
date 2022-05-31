from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import askyesno

import config


class AccountInfoView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.viewed_account_id = None
        self.controller = controller
        self.login_text_field = None
        self.password_text_field = None
        self.games_name_text_field = None
        self.platform_text_field = None
        self.additional_text_field = None
        self.added_date_text_field = None
        self.delete_button = None
        self.__setup()

    def __setup(self):
        FONTSIZE_TEXT = config.app['font_text']
        FONTSIZE_LABEL = config.app['font_label']

        account_lbl = tk.Label(self, text='Account Info', font=(None, 30, 'bold'))
        self.login_text_field = tk.Text(self, state='disabled', height=1, font=FONTSIZE_TEXT)
        self.password_text_field = tk.Text(self, state='disabled', height=1, font=FONTSIZE_TEXT)
        self.games_name_text_field = tk.Text(self, state='disabled', height=2, font=FONTSIZE_TEXT)
        self.platform_text_field = tk.Text(self, state='disabled', height=1, font=FONTSIZE_TEXT)
        self.additional_text_field = tk.Text(self, state='disabled', height=4, font=FONTSIZE_TEXT)
        self.added_date_text_field = tk.Text(self, state='disabled', height=1, font=FONTSIZE_TEXT)
        self.delete_button = tk.Button(self, text='Delete Account', command=self.delete_account, font=FONTSIZE_LABEL)

        account_lbl.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(self, text='Login', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.login_text_field.pack(side=tk.TOP, fill=tk.BOTH, pady=10)
        tk.Label(self, text='Password', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.password_text_field.pack(side=tk.TOP, fill=tk.BOTH, pady=10)
        tk.Label(self, text='Game', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.games_name_text_field.pack(side=tk.TOP, fill=tk.BOTH, pady=10)
        tk.Label(self, text='Platform', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.platform_text_field.pack(side=tk.TOP, fill=tk.BOTH, pady=10)
        tk.Label(self, text='Additional Information', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.additional_text_field.pack(side=tk.TOP, fill=tk.BOTH, pady=10)
        tk.Label(self, text='Added Date', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.added_date_text_field.pack(side=tk.TOP, fill=tk.BOTH, pady=10)
        self.delete_button.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def set_account_info(self, account):
        self.viewed_account_id = account.id
        self.__insert_text_to_text_field(self.login_text_field, account.login)
        self.__insert_text_to_text_field(self.password_text_field, '*' * 10)
        self.__insert_text_to_text_field(self.games_name_text_field, account.game.name)
        self.__insert_text_to_text_field(self.platform_text_field, account.platform.name)
        self.__insert_text_to_text_field(self.additional_text_field, account.additional_information)
        self.__insert_text_to_text_field(self.added_date_text_field, account.added_date)

    def __insert_text_to_text_field(self, text_field: tk.Text, text):
        text_field.configure(state='normal')
        text_field.delete(1.0, tk.END)
        text_field.tag_configure("center", justify='center')
        text_field.insert(1.0, text, 'center')
        text_field.configure(state='disabled')

    def clear_all(self):
        self.__insert_text_to_text_field(self.login_text_field, '')
        self.__insert_text_to_text_field(self.password_text_field, '')
        self.__insert_text_to_text_field(self.games_name_text_field, '')
        self.__insert_text_to_text_field(self.platform_text_field, '')
        self.__insert_text_to_text_field(self.additional_text_field, '')
        self.__insert_text_to_text_field(self.added_date_text_field, '')

    def delete_account(self):
        if self.viewed_account_id:
            answer = askyesno(title='Delete confirmation', message='Are you sure you want to delete this account?')
            if answer:
                self.controller.delete_account(self.viewed_account_id)
