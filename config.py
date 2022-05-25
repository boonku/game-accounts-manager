import os.path

database = {
    'name': 'game-accounts-manager.db'
}

script = {
    'name': 'create_tables.sql'
}

encryption = {
    'file': 'secret.key'
}

app = {
    'title': 'Game Accounts Manager',
    # application's window width, height
    'size': (1000, 800),
    'max_size': (1920, 1080),
    'min_size': (600, 500),
    'window_icon': 'resources/app-icon.ico',
    'root_dir': os.path.dirname(os.path.abspath(__file__)) + '/'
}
