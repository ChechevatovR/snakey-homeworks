#!/usr/bin/python

import sys
import click

@click.command()
@click.argument("files", type=click.File("r"), nargs=-1)
@click.option("-n", default=10)
def cli(files, n: int):
    if len(files) == 0:
        impl([sys.stdin], 17, False)
        return
    impl(files, n, len(files) > 1)


def impl(files, n: int, print_filename: bool):
    for file in files:
        lines = file.readlines()
        tail = lines[-n:]
        tail = map(str.rstrip, tail)
        if print_filename:
            print(f'==> {file.name} <==')
        for line in tail:
            print(line)

if __name__ == "__main__":
    cli()
