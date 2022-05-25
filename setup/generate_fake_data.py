from os.path import exists
from faker import Faker
from database.Database import Database
from model.Account import Account
from model.Game import Game
from random import choice
import config

if not exists(config.app['root_dir'] + config.database['name']):
    print('no database found, generate it with setup script')
    exit(1)

db = Database()
platforms = db.get_platforms()

fake = Faker()
Faker.seed(0)

# random game names
games = [
    'Minecraft',
    'Assassin\'s Creed Valhalla',
    'Cyberpunk 2077',
    'Assassin\'s Creed Origin',
    'Witcher 3',
    'Baldur\'s Gate III',
    'Assassin\'s Creed Odyssey',
    'Dying Light',
    'Last Epoch',
    'Resident Evil Village',
    'DEATHLOOP',
    'Borderlands 3 Ultimate Edition',
    'Witcher 2',
    'Sims 4',
    'Elden Ring',
    'Dragon\'s Dogma',
    'Dark Souls I',
    'GTA V',
    'Monster Hunter World',
    'GTA IV',
    'Dark Souls III',
    'Tiny Tina\'s Wonderlands',
    'Forspoken',
    'Sniper Elite 5',
    'Dying Light',
    'Dying Light 2 Stay Human',
    'God of War',
    'Far Cry 6',
    'Immortals Fenyx Rising',
    'Need for Speed',
    'DIRT 5',
    'Battlefield V',
    'STAR WARS Jedi: Fallen Order'
]

# create random information for accounts
accounts = []
for i in range(100):
    accounts.append(
        (fake.ascii_free_email(), fake.text(max_nb_chars=10), Game(0, choice(games)),
         choice(platforms), fake.text(max_nb_chars=20))
    )

# insert accounts to database
for acc in accounts:
    account = Account.create_account(0, *acc)
    print(f'Inserting: {account}')
    db.save_account(account)
