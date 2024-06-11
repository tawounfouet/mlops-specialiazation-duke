#!/usr/bin/env python
"""Marco Polo

"""
import click


def marco(name):
    if name == "Marco":
        return "Polo"
    return "No"


def polo(name):
    if name == "Polo":
        return "Yes"
    return "No"


@click.group()
def cli():
    pass


@cli.command("phrase")
@click.argument("name")
def marco_cli(name):
    """
    Say Marco
    Example: ./marco_polo.py phrase Marco
    """
    # if name == "Marco": echo green color otherwise red
    click.echo(click.style(marco(name), fg="green" if marco(name) == "Polo" else "red"))


if __name__ == "__main__":
    cli()
