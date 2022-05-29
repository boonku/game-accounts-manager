import tkinter as tk

import config


class AddAccountView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.container = parent
        self.controller = controller
        self.login_field = None
        self.password_field = None
        self.game_field = None
        self.platform_field = None
        self.additional_info_field = None
        self.submit_button = None
        self.cancel_button = None
        self.__setup()

    def __setup(self):
        self.title('Add New Account')
        self.transient(self.container)
        self.grab_set()
        self.geometry('350x500')
        self.resizable(False, False)
        self.configure(padx=20, pady=20)
        FONTSIZE_TEXT = config.app['font_text']
        FONTSIZE_LABEL = config.app['font_label']
        tk.Label(self, text='Login', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.login_field = tk.Entry(self, font=FONTSIZE_TEXT)
        self.login_field.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(self, text='Password', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.password_field = tk.Entry(self, show='*', font=FONTSIZE_TEXT)
        self.password_field.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(self, text='Game', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.game_field = tk.Entry(self, font=FONTSIZE_TEXT)
        self.game_field.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(self, text='Platform', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.platform_field_value = tk.StringVar()
        self.platform_field = tk.OptionMenu(self, self.platform_field_value,
                                            *[platform.name for platform in self.controller.get_platforms()])
        self.platform_field.config(font=FONTSIZE_TEXT)
        self.platform_field.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(self, text='Additional Information', font=FONTSIZE_LABEL).pack(side=tk.TOP, fill=tk.BOTH)
        self.additional_info_field = tk.Text(self, font=FONTSIZE_TEXT, height=4)
        self.additional_info_field.pack(side=tk.TOP, fill=tk.BOTH)
        self.cancel_button = tk.Button(self, text='Cancel', command=self.destroy)
        self.cancel_button.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.submit_button = tk.Button(self, text='Add Account', command=self.submit_account)
        self.submit_button.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def submit_account(self):
        login = self.login_field.get()
        password = self.password_field.get()
        game = self.game_field.get()
        platform = self.platform_field_value.get()
        additional_information = self.additional_info_field.get(1.0, tk.END)
        success = self.controller.add_account(login, password, game, platform, additional_information)
        if success:
            self.destroy()
