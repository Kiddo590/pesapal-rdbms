from core.storage.file_manager import write_row, read_rows

class Table:
    def __init__(self, name, schema):
        self.name = name
        self.schema = schema

    def insert(self, row):
        write_row(self.name, row)

    def all(self):
        return read_rows(self.name)
