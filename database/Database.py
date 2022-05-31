import sqlite3
import config
from model.Account import Account
from model.Game import Game
from model.Platform import Platform


class Database:
    def __init__(self):
        root_dir = config.app['root_dir']
        db_name = config.database['name']
        self.connection = sqlite3.connect(root_dir + db_name)

    def get_connection(self):
        return self.connection

    def save_account(self, account):
        cursor = self.connection.cursor()
        sql_acc = '''
            INSERT INTO Accounts(Login, Password, Game, Platform, AdditionalInformation, DateAdded)
            VALUES(?, ?, ?, ?, ?, ?);
        '''
        game = self.get_game_from_name(account.game.name)
        platform_id = account.platform.id
        if not game:
            game_id = self.save_game(account.game)
        else:
            game_id = game.id
        cursor.execute(sql_acc, (account.login, account.password, game_id, platform_id,
                                 account.additional_information, account.date_added))
        self.connection.commit()
        return cursor.lastrowid

    def get_accounts(self):
        sql = '''
            SELECT
                AccountId,
                Login,
                Password,
                GameId,
                GameName,
                PlatformId,
                platformName,
                AdditionalInformation,
                DateAdded
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
                GameId,
                GameName,
                PlatformId,
                platformName,
                AdditionalInformation,
                DateAdded
            FROM
                Accounts
            INNER JOIN Games on Accounts.Game = Games.GameId
            INNER JOIN Platforms on Accounts.Platform = Platforms.PlatformId
            WHERE AccountId = ?;
        '''
        cursor = self.connection.cursor()
        result = cursor.execute(sql, (account_id,))
        return self.__map_row_to_acc(result.fetchone())

    def delete_account(self, account_id):
        sql_delete_account = 'DELETE FROM Accounts WHERE AccountId=?;'
        account = self.get_account(account_id)
        sql_get_game = 'SELECT COUNT(*) FROM Accounts WHERE Game=?'
        cursor = self.connection.cursor()
        number_of_accounts_with_game = cursor.execute(sql_get_game, (account.game.id,)).fetchone()[0]
        # delete game from database if there won't be any account using it
        if number_of_accounts_with_game == 1:
            self.delete_game(account.game.id)
        cursor.execute(sql_delete_account, (account_id,))
        self.connection.commit()

    def edit_additional_information(self, account_id, additional_information):
        sql = 'UPDATE Accounts SET AdditionalInformation=? WHERE AccountId=?'
        cursor = self.connection.cursor()
        cursor.execute(sql, (additional_information, account_id))
        self.connection.commit()

    def save_game(self, game):
        sql = 'INSERT INTO Games(GameName) VALUES (?);'
        cursor = self.connection.cursor()
        cursor.execute(sql, (game.name,))
        self.connection.commit()
        return cursor.lastrowid

    def get_games(self):
        sql = 'SELECT * FROM Games;'
        cursor = self.connection.cursor()
        result = cursor.execute(sql)
        games = []
        for game in result:
            games.append(self.__map_row_to_game(game))
        return games

    def delete_game(self, game_id):
        sql = 'DELETE FROM Games WHERE GameId=?'
        cursor = self.connection.cursor()
        cursor.execute(sql, (game_id,))
        self.connection.commit()

    def get_game_from_id(self, game_id):
        sql = 'SELECT * FROM Games WHERE GameId = ?;'
        cursor = self.connection.cursor()
        row = cursor.execute(sql, (game_id,)).fetchone()
        return self.__map_row_to_game(row)

    def get_game_from_name(self, game_name):
        sql = 'SELECT * FROM Games WHERE GameName = ?;'
        cursor = self.connection.cursor()
        row = cursor.execute(sql, (game_name,)).fetchone()
        return self.__map_row_to_game(row)

    def get_platforms(self):
        sql = 'SELECT * FROM Platforms;'
        cursor = self.connection.cursor()
        result = cursor.execute(sql)
        platforms = []
        for platform in result:
            platforms.append(self.__map_row_to_platform(platform))
        return platforms

    def get_platform_from_id(self, platform_id):
        sql = 'SELECT * FROM Platforms WHERE PlatformId = ?;'
        cursor = self.connection.cursor()
        row = cursor.execute(sql, (platform_id,)).fetchone()
        return self.__map_row_to_platform(row)

    def get_platform_from_name(self, platform_name):
        sql = 'SELECT * FROM Platforms WHERE PlatformName = ?;'
        cursor = self.connection.cursor()
        row = cursor.execute(sql, (platform_name,)).fetchone()
        return self.__map_row_to_platform(row)

    def __map_row_to_acc(self, row):
        game = Game(row[3], row[4])
        platform = Platform(row[5], row[6])
        return Account(row[0], row[1], row[2].decode('utf-8'), game, platform, row[7], row[8])

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
