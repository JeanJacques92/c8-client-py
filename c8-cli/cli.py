#!/usr/bin/env python

"""_summary_

"""

from typing_extensions import Annotated

import typer
from plmprovider import C8Instance
from attributes import plm_attributes

app = typer.Typer()


@app.command()
def c8_client():
    """_summary_"""
    print("client")
    c8inst = C8Instance("http://", "user", "password")
    print(c8inst.c8_info())


@app.command()
def connect_plm(
    url: Annotated[str, typer.Option("--server", "-s")],
    user: Annotated[str, typer.Option("--user", "-u")],
    pwd: Annotated[str, typer.Option("--password", "-p")],
    debug: bool = typer.Option(False, help="Enable debug mode"),
    renew: bool = typer.Option(False,"--renew","-r", help="Renew the token"),
):
    """Connect to plm 

    Args:
        url (Annotated[str, typer.Option): _description_
        user (Annotated[str, typer.Option): _description_
        pwd (Annotated[str, typer.Option): _description_
    """
    c8inst = C8Instance(url, user, pwd)
    if debug:
        typer.echo(f"{user}, {pwd}")
    result = c8inst.connect(renew)

    print(str(result))
    plm_attributes.count_attributes(c8inst)

if __name__ == "__main__":
    app()
