from database.Database import Database
from encryption import encryption
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

    def decode_password(self, account):
        decoded_password = encryption.decrypt_message(account.password.encode())
        return decoded_password

    def set_account_info(self, account_id):
        account = self.get_account(account_id)
        self.account_info_view.set_account_info(account)
