import os.path

database = {
    'name': 'game-accounts-manager.db'
}

script = {
    'name': 'setup/create_tables.sql'
}

encryption = {
    'file': 'secret.key'
}

app = {
    'title': 'Game Accounts Manager',
    # application's window width, height
    'size': (1000, 800),
    'max_size': (1920, 1080),
    'min_size': (1000, 800),
    'window_icon': 'resources/app-icon.ico',
    'add_account_icon': 'resources/add-account-icon.ico',
    'root_dir': os.path.dirname(os.path.abspath(__file__)) + '/',
    'font_text': (None, 13, ),
    'font_label': (None, 15, 'bold')
}
