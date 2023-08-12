#!/usr/bin/env python

"""_summary_

"""
import time
import json
from itertools import tee
from concurrent.futures import ThreadPoolExecutor
from rich.progress import Progress
from typing_extensions import Annotated

import typer
from plmprovider import C8Instance
app = typer.Typer()

@app.command()
def c8_client ():
    """_summary_
    """
    print("client")
    c8inst = C8Instance("http://","user","password")
    print (c8inst.c8_info())

if __name__ == "__main__":
    app()
