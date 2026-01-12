from rich.console import Console
from rich.prompt import Prompt

console = Console()

def start_repl():
    console.print("[bold green]Pesapal RDBMS v1.0[/bold green]")
    console.print("Type 'exit' to quit\n")

    while True:
        try:
            query = Prompt.ask("[bold blue]pesapal-db>[/bold blue]")

            if query.lower() in ("exit", "quit"):
                console.print("Goodbye 👋")
                break

            console.print(f"[yellow]SQL received:[/yellow] {query}")

        except KeyboardInterrupt:
            console.print("\nGoodbye 👋")
            break
