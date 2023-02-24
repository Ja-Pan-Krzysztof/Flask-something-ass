from sqlite3 import connect


def connection(name: str):
    return connect(f'{name}.db')
