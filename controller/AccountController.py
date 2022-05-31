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

    def add_account(self, login, password, game_name, platform_name, additional_information):
        platform = self.db.get_platform_from_name(platform_name)
        if not platform:
            return False
        game = Game(0, game_name)
        if login == '' or password == '' or game_name == '':
            return False
        account = Account.create_account(0, login, password, game, platform, additional_information)
        self.db.save_account(account)
        self.clear()
        return True

    def delete_account(self, account_id):
        self.db.delete_account(account_id)
        self.clear()

    def get_platforms(self):
        return self.db.get_platforms()

    def decode_password(self, account):
        decoded_password = encryption.decrypt_message(account.password.encode())
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

    def clear(self):
        self.accounts_table_view.clear_all()
        self.accounts_table_view.insert_all()
        self.account_info_view.clear_all()
