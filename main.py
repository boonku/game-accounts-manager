import tkinter as tk
import config

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
        print('no database found, generate it with setup script')
        exit(1)


def check_for_secret():
    if not exists(config.app['root_dir'] + 'secret.key'):
        print('no key found, generate it with setup script')
        exit(2)


if __name__ == '__main__':
    main()
