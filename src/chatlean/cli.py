"""CLI entrypoint for chatlean."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatlean import __version__


@click.group(name="chatlean", invoke_without_command=True)
@click.version_option(__version__, prog_name="chatlean")
@add_tree_option
@click.pass_context
def main(ctx: click.Context) -> None:
    """chatlean command line interface."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()
