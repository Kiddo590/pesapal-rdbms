from core.catalog.schema import Column, TableSchema
from core.engine.database import Database
from core.parser.ast import CreateTable, Insert, Select

class Executor:
    def __init__(self, database: Database):
        self.db = database

    def execute(self, ast):
        if isinstance(ast, CreateTable):
            return self._create_table(ast)
        elif isinstance(ast, Insert):
            return self._insert(ast)
        elif isinstance(ast, Select):
            return self._select(ast)
        else:
            raise NotImplementedError(f"Execution not supported for {type(ast)}")

    # ---------------- CREATE TABLE ----------------

    def _create_table(self, ast: CreateTable):
        columns = []
        for col in ast.columns:
            columns.append(Column(
                name=col.name,
                col_type=col.col_type,
                primary=col.primary,
                unique=col.unique
            ))

        schema = TableSchema(ast.table_name, columns)
        self.db.create_table(schema)

        return f"Table '{ast.table_name}' created successfully"

    # ---------------- INSERT ----------------

    def _insert(self, ast: Insert):
        table = self.db.get_table(ast.table_name)

        if len(ast.values) != len(table.schema.columns):
            raise ValueError("Column count does not match values count")

        row = {}
        for col, val in zip(table.schema.columns, ast.values):
            row[col.name] = val

        table.insert(row)

        return "1 row inserted"

    # ---------------- SELECT ----------------

    def _select(self, ast: Select):
        table = self.db.get_table(ast.table_name)
        rows = table.all()

        if ast.columns == ["*"]:
            return rows

        result = []
        for row in rows:
            filtered = {col: row[col] for col in ast.columns}
            result.append(filtered)

        return result
