#!/usr/bin/python

from itertools import chain
import click

@click.command()
@click.argument("files", type=click.File("r"), nargs=-1)
def cli(files):
    for line_no, line in enumerate(map(lambda line: line.rstrip(), chain.from_iterable(map(lambda file: file.readlines(), files))), start=1):
        print(f"{line_no:>6}\t{line}")


if __name__ == "__main__":
    cli()
