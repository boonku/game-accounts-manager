import tkinter as tk
from tkinter.messagebox import showerror

from view.ExportImportTemplate import ExportImportTemplate


class ExportAccountView(ExportImportTemplate):
    def __init__(self, parent, controller, account_id):
        super().__init__(parent, controller)
        self.account_id = account_id
        self.code = None
        self.__setup()

    def __setup(self):
        self.title('Export Account')
        self.button.config(text='Export Account', command=self.export_account)
        self.code_field.config(state='disable')
        self.message = tk.Label(self, text='Copied code to clipboard', fg='#00ff00')

    def export_account(self):
        password = self.password_field.get().strip()
        if password and password != '':
            self.code = self.controller.export_account(self.account_id, password)
            self.code_field.config(state='normal')
            self.code_field.delete(1.0, tk.END)
            self.code_field.insert(1.0, self.code)
            self.code_field.config(state='disable')
            self.password_field.config(state='disable')
            self.button.config(text='Copy code', command=self.copy_code)
            self.cancel_button.config(text='Exit')
        else:
            showerror(title='Error', message='Type in non-empty password')

    def copy_code(self):
        self.container.clipboard_clear()
        self.container.clipboard_append(self.code)
        self.message.pack(side=tk.BOTTOM, fill=tk.BOTH)
