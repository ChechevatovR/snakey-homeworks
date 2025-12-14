#!/usr/bin/python

import sys
import click

@click.command()
@click.argument("files", type=click.File("rb"), nargs=-1)
def cli(files):
    if len(files) == 0:
        impl([sys.stdin.buffer], False, False)
        return
    impl(files, True, len(files) > 1)


def impl(files, print_filename: bool, print_total: bool):
    totalBytes = 0
    totalWords = 0
    totalLines = 0
    for file in files:
        content = file.read()
        bytes = len(content)
        newlines = content.count(b"\n")
        words = len(content.split())
        if print_filename:
            print(newlines, words, bytes, file.name, sep="\t")
        else:
            print(newlines, words, bytes, sep="\t")
        totalBytes += bytes
        totalWords += words
        totalLines += newlines
    if print_total:
        print(totalLines, totalWords, totalBytes, 'total', sep='\t')

if __name__ == "__main__":
    cli()
