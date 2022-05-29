import tkinter as tk
import config
from setup import setup
from view.MainView import MainView
from os.path import exists


def main():
    check_for_db()
    check_for_secret()

    root = tk.Tk()
    root.title(config.app['title'])
    root.iconbitmap(config.app['window_icon'])
    width, height = (config.app['size'])
    root.geometry('%sx%s' % (width, height))
    root.minsize(*config.app['min_size'])
    root.maxsize(*config.app['max_size'])
    view = MainView(root)
    root.mainloop()


def check_for_db():
    if not exists(config.app['root_dir'] + config.database['name']):
        setup.create_db()


def check_for_secret():
    if not exists(config.app['root_dir'] + 'secret.key'):
        setup.create_key()


if __name__ == '__main__':
    main()
