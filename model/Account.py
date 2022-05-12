from datetime import date


class Account:
    def __init__(self,id,  login, password, game, platform, additional_information='', added_date=date.today()):
        self.id = id
        self.login = login
        self.password = password
        self.game = game
        self.platform = platform
        self.additional_information = additional_information
        self.added_date = added_date

    def __str__(self) -> str:
        return f'Account{{' \
               f'id={self.id}, ' \
               f'login={self.login}, ' \
               f'password={self.password}, ' \
               f'game={self.game}, ' \
               f'platform={self.platform}, ' \
               f'addit_info={self.additional_information}, ' \
               f'added_date={self.added_date}}}'

