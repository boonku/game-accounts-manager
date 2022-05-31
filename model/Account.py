from encryption import encryption
from datetime import date


class Account:
    def __init__(self, id, login, password, game, platform, additional_information='', date_added=date.today()):
        self.id = id
        self.login = login
        self.password = password
        self.game = game
        self.platform = platform
        self.additional_information = additional_information
        self.date_added = date_added

    @classmethod
    def create_account(cls, id, login, password, game, platform, additional_information='', date_added=date.today()):
        # encrypt password
        password = encryption.encrypt_message(password)
        return cls(id, login, password, game, platform, additional_information, date_added)

    def __str__(self) -> str:
        return f'Account{{' \
               f'id={self.id}, ' \
               f'login={self.login}, ' \
               f'password={self.password}, ' \
               f'game={self.game}, ' \
               f'platform={self.platform}, ' \
               f'addit_info={self.additional_information}, ' \
               f'date_added={self.date_added}}}'
