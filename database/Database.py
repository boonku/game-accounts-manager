import sqlite3
import config
from model.Account import Account
from model.Game import Game
from model.Platform import Platform


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(config.database['name'])

    def get_connection(self):
        return self.connection

    def save_account(self, account):
        cursor = self.connection.cursor()
        sql_acc = '''
            INSERT INTO Accounts(Login, Password, Game, Platform, AdditionalInformation, AddedDate)
            VALUES(?, ?, ?, ?, ?, ?);
        '''
        game = self.get_game(account.game.name)
        platform_id = account.platform.id
        if not game:
            game_id = self.save_game(account.game)
        else:
            game_id = game.id
        self.connection.execute(sql_acc, (account.login, account.password, game_id, platform_id,
                                          account.additional_information, account.added_date))
        self.connection.commit()
        return cursor.lastrowid

    def get_accounts(self):
        sql = '''
            SELECT
                AccountId,
                Login,
                Password,
                GameName,
                platformName,
                AdditionalInformation,
                AddedDate
            FROM
                Accounts
            INNER JOIN Games on Accounts.Game = Games.GameId
            INNER JOIN Platforms on Accounts.Platform = Platforms.PlatformId;
        '''
        cursor = self.connection.cursor()
        result = cursor.execute(sql)
        accounts = []
        for row in result:
            acc = self.__map_row_to_acc(row)
            accounts.append(acc)
        return accounts

    def get_account(self, account_id):
        sql = '''
            SELECT
                AccountId,
                Login,
                Password,
                GameName,
                platformName,
                AdditionalInformation,
                AddedDate
            FROM
                Accounts
            INNER JOIN Games on Accounts.Game = Games.GameId
            INNER JOIN Platforms on Accounts.Platform = Platforms.PlatformId
            WHERE AccountId = ?;
        '''
        cursor = self.connection.cursor()
        result = cursor.execute(sql, (account_id,))
        return self.__map_row_to_acc(result.fetchone())

    def save_game(self, game):
        sql = 'INSERT INTO Games(GameName) VALUES (?)'
        cursor = self.connection.cursor()
        cursor.execute(sql, (game.name,))
        self.connection.commit()
        return cursor.lastrowid

    def get_games(self):
        sql = 'SELECT * FROM Games'
        cursor = self.connection.cursor()
        result = cursor.execute(sql)
        games = []
        for game in result:
            games.append(self.__map_row_to_game(game))
        return games

    def get_game(self, game_id):
        sql = 'SELECT * FROM Games WHERE GameId = ?'
        cursor = self.connection.cursor()
        row = cursor.execute(sql, (game_id,)).fetchone()
        return self.__map_row_to_game(row)

    def get_game(self, game_name):
        sql = 'SELECT * FROM Games WHERE GameName = ?'
        cursor = self.connection.cursor()
        row = cursor.execute(sql, (game_name, )).fetchone()
        return self.__map_row_to_game(row)

    def get_platforms(self):
        sql = 'SELECT * FROM Platforms'
        cursor = self.connection.cursor()
        result = cursor.execute(sql)
        platforms = []
        for platform in result:
            platforms.append(self.__map_row_to_platform(platform))
        return platforms

    def get_platform(self, platform_id):
        sql = 'SELECT * FROM Platforms WHERE PlatformId = ?'
        cursor = self.connection.cursor()
        row = cursor.execute(sql, (platform_id, )).fetchone()
        return self.__map_row_to_platform(row)

    def __map_row_to_acc(self, row):
        if row:
            return Account(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return None

    def __map_row_to_game(self, row):
        if row:
            return Game(row[0], row[1])
        return None

    def __map_row_to_platform(self, row):
        if row:
            return Platform(row[0], row[1])
        return None

    def close(self):
        if self.connection:
            self.connection.close()
