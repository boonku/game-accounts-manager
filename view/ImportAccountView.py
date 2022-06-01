import tkinter as tk
from tkinter.messagebox import showinfo, showerror

from view.ExportImportTemplate import ExportImportTemplate


class ImportAccountExportImport(ExportImportTemplate):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.__setup()

    def __setup(self):
        self.button.config(text='Import Account', command=self.import_account)

    def import_account(self):
        password = self.password_field.get().strip()
        code = self.code_field.get(1.0, tk.END).strip()
        if not password or password == '':
            showerror(title='Error', message='Type in password')
        elif not code or code == '':
            showerror(title='Error', message='Type in code')
        else:
            success = self.controller.import_account(code, password)
            if success:
                showinfo(title='Success', message='Successfully imported account from code')
                self.destroy()
            else:
                showerror(title='Error', message='Incorrect code or password')
