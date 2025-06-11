import typer
from engine import ask_devops_helper, translate_command, get_logs

app = typer.Typer()

@app.command()
def ask(prompt: str):
    """Ask the AI DevOps Helper a question."""
    response = ask_devops_helper(prompt)
    typer.echo(response)

@app.command()
def translate(prompt: str):
    """Translate a natural language command to shell."""
    command = translate_command(prompt)
    typer.echo(command)

@app.command()
def logs(service: str):
    """Fetch logs for a specific service."""
    output = get_logs(service)
    typer.echo(output)

if __name__ == "__main__":
    app()