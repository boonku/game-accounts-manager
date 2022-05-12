class Game:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f'Game{{' \
               f'id={self.id}, ' \
               f'name={self.name}}}'
