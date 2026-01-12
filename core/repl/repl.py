from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table as RichTable

from core.parser.tokenizer import tokenize
from core.parser.parser import parse
from core.engine.executor import Executor
from core.engine.database import Database

console = Console()
db = Database()
executor = Executor(db)

def display_rows(rows):
    if not rows:
        console.print("[italic]No rows returned[/italic]")
        return

    table = RichTable(show_header=True, header_style="bold magenta")
    for col in rows[0].keys():
        table.add_column(col)

    for row in rows:
        table.add_row(*[str(v) for v in row.values()])

    console.print(table)

def start_repl():
    console.print("[bold green]Pesapal RDBMS v1.0[/bold green]")
    console.print("Type 'exit' to quit\n")

    while True:
        try:
            query = Prompt.ask("[bold blue]pesapal-db>[/bold blue]")

            if query.lower() in ("exit", "quit"):
                console.print("Goodbye 👋")
                break

            tokens = tokenize(query)
            ast = parse(tokens)
            result = executor.execute(ast)

            if isinstance(result, list):
                display_rows(result)
            else:
                console.print(f"[green]{result}[/green]")

        except Exception as e:
            console.print(f"[red]ERROR:[/red] {e}")
