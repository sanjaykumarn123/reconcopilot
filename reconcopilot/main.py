from .core import ingest_file

@app.command()
def ingest(
    filepath: str,
    source: str = typer.Option(..., help="subfinder | httpx | katana | nuclei | burp"),
    target: str = typer.Option(..., help="Program name, e.g. 'acme-bugbounty'"),
):
    """Ingest recon output into the database."""
    if not typer.confirm(f"Confirm you are authorized to test targets under '{target}'?"):
        console.print("[red]Aborted — ingestion requires authorized scope.[/red]")
        raise typer.Exit(code=1)

    try:
        count = ingest_file(filepath, source, target)
        console.print(f"[bold green]Ingested {count} endpoints[/bold green] from {source} into '{target}'")
    except ValueError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(code=1)