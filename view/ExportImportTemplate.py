import tkinter as tk

import config


class ExportImportTemplate(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.container = parent
        self.controller = controller
        self.password_field = None
        self.code_field = None
        self.button = None
        self.cancel_button = None
        self.message = None
        self.__setup()

    def __setup(self):
        self.__setup_window()
        self.__setup_widgets()

    def __setup_window(self):
        self.transient(self.container)
        self.grab_set()
        self.geometry('350x500')
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

    def __setup_widgets(self):
        FONTSIZE_TEXT = config.app['font_text']
        FONTSIZE_LABEL = config.app['font_label']
        self.password_field = tk.Entry(self, font=FONTSIZE_TEXT)
        self.code_field = tk.Text(self, height=4, font=FONTSIZE_TEXT)
        tk.Label(self, text='Password', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.password_field.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(self, text='Code', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.code_field.pack(side=tk.TOP, fill=tk.BOTH)
        self.cancel_button = tk.Button(self, text='Cancel', font=FONTSIZE_LABEL, command=self.cancel)
        self.cancel_button.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.button = tk.Button(self, text='Placeholder', font=FONTSIZE_LABEL)
        self.button.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def cancel(self):
        self.destroy()
