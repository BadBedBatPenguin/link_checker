from typing import List, Optional
import typer
from .script import links_checker

__app_name__ = "links_checker"
__version__ = "0.1.0s"

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.command()
def get(
    links: List[str] = typer.Argument(...)
):
    typer.secho(f'{links_checker(links)}')

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
