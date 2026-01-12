from core.parser.ast import (
    CreateTable,
    ColumnDef,
    Insert,
    Select
)

class SQLParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # ------------------ UTILITIES ------------------

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected=None):
        token = self.current()
        if token is None:
            raise SyntaxError("Unexpected end of input")

        if expected and token != expected:
            raise SyntaxError(f"Expected '{expected}', got '{token}'")

        self.pos += 1
        return token

    # ------------------ ENTRY POINT ------------------

    def parse(self):
        token = self.current()

        if token == "CREATE":
            return self.parse_create_table()
        elif token == "INSERT":
            return self.parse_insert()
        elif token == "SELECT":
            return self.parse_select()
        else:
            raise SyntaxError(f"Unknown command '{token}'")

    # ------------------ CREATE TABLE ------------------

    def parse_create_table(self):
        self.consume("CREATE")
        self.consume("TABLE")

        table_name = self.consume()

        self.consume("(")

        columns = []
        while True:
            col_name = self.consume()
            col_type = self.consume()

            primary = False
            unique = False

            while self.current() in ("PRIMARY", "UNIQUE"):
                if self.current() == "PRIMARY":
                    self.consume("PRIMARY")
                    self.consume("KEY")
                    primary = True
                elif self.current() == "UNIQUE":
                    self.consume("UNIQUE")
                    unique = True

            columns.append(ColumnDef(
                name=col_name,
                col_type=col_type,
                primary=primary,
                unique=unique
            ))

            if self.current() == ",":
                self.consume(",")
                continue
            break

        self.consume(")")

        return CreateTable(table_name, columns)

    # ------------------ INSERT ------------------

    def parse_insert(self):
        self.consume("INSERT")
        self.consume("INTO")

        table_name = self.consume()

        self.consume("VALUES")
        self.consume("(")

        values = []
        while True:
            token = self.consume()
            if token.startswith("'"):
                values.append(token.strip("'"))
            elif token.isdigit():
                values.append(int(token))
            else:
                values.append(token)

            if self.current() == ",":
                self.consume(",")
                continue
            break

        self.consume(")")

        return Insert(table_name, values)

    # ------------------ SELECT ------------------

    def parse_select(self):
        self.consume("SELECT")

        columns = []
        while True:
            token = self.consume()
            if token == "FROM":
                break
            if token != ",":
                columns.append(token.lower())

        table_name = self.consume()

        return Select(columns, table_name)


# ---------- HELPER FUNCTION ----------

def parse(tokens):
    parser = SQLParser(tokens)
    return parser.parse()
