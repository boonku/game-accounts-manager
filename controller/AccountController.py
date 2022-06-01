import json
from datetime import date

import cryptography.fernet

from database.Database import Database
from encryption import encryption
from model.Account import Account
from model.Game import Game
from view import AccountTableView, AccountInfoView


class AccountController:
    def __init__(self):
        self.db = Database()
        self.accounts_table_view: AccountTableView = None
        self.account_info_view: AccountInfoView = None

    def get_accounts(self):
        return self.db.get_accounts()

    def get_account(self, account_id):
        return self.db.get_account(account_id)

    def add_account(self, login, password, game_name, platform_name, additional_information, date_added=date.today()):
        platform = self.db.get_platform_from_name(platform_name)
        if not platform:
            return -1
        game = Game(0, game_name)
        if login == '' or password == '' or game_name == '':
            return -1
        account = Account.create_account(0, login, password, game, platform, additional_information, date_added)
        id = self.db.save_account(account)
        self.clear()
        return id

    def delete_account(self, account_id):
        self.db.delete_account(account_id)
        self.clear()

    def get_platforms(self):
        return self.db.get_platforms()

    def decode_password(self, account):
        decoded_password = encryption.decrypt_message(account.password.encode()).decode('utf-8')
        return decoded_password

    def get_plain_password(self, account_id):
        account = self.get_account(account_id)
        if account:
            return self.decode_password(account)
        return ''

    def set_account_info(self, account_id):
        account = self.get_account(account_id)
        self.account_info_view.set_account_info(account)

    def edit_accounts_add_info(self, account_id, additional_information):
        self.db.edit_additional_information(account_id, additional_information)
        self.set_account_info(account_id)

    def cancel_edit(self, account_id):
        self.set_account_info(account_id)

    def clear(self):
        self.accounts_table_view.clear_all()
        self.accounts_table_view.insert_all()
        self.account_info_view.clear_all()

    def export_account(self, account_id, user_password):
        if not account_id:
            return
        account = self.get_account(account_id)
        if not account:
            return
        decoded_password = self.decode_password(account)
        account.password = decoded_password
        account_json = json.dumps(account, default=lambda o: o.__dict__)
        encrypted_account = encryption.password_encrypt(account_json.encode(), user_password)
        return encrypted_account

    def import_account(self, encrypted_account, user_password):
        try:
            account = json.loads(encryption.password_decrypt(encrypted_account, user_password))
        except (cryptography.fernet.InvalidToken, cryptography.fernet.InvalidSignature):
            return False

        account_id = self.add_account(account['login'],
                                      account['password'],
                                      account['game']['name'],
                                      account['platform']['name'],
                                      account['additional_information'],
                                      account['date_added']
                                      )
        self.set_account_info(account_id)
        return True
