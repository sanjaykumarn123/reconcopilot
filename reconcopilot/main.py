import typer
from rich.console import Console

app = typer.Typer(help="AI-powered bug bounty recon copilot")
console = Console()

@app.command()
def hello():
    """Sanity-check command."""
    console.print("[bold green]ReconCopilot is alive[/bold green]")

if __name__ == "__main__":
    app()