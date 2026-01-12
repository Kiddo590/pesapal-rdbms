from core.storage.table import Table

class Database:
    def __init__(self):
        self.tables = {}  # table_name -> Table

    def create_table(self, schema):
        if schema.name in self.tables:
            raise ValueError(f"Table '{schema.name}' already exists")

        table = Table(schema.name, schema)
        self.tables[schema.name] = table

    def get_table(self, table_name):
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist")
        return self.tables[table_name]
