import pickle
from tabulate import tabulate


def load_table(file_path, delimiter=';'):
    with open(file_path, 'rb') as f:
        return pickle.load(f)


def save_table(table, filename, delimiter=';'):
    with open(filename, 'wb') as f:
        pickle.dump(table, f)
