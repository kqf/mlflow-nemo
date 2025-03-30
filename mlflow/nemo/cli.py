import click

from mlflow.cli import cli


@cli.group()
def nemo():
    """Nemo plugin for MLflow."""
    pass


@nemo.command()
@click.option("--name", default="world", help="Name to greet.")
def hello(name):
    """Simple command to test the plugin."""
    click.echo(f"Hello, {name}!")
