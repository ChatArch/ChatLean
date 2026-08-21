from click.testing import CliRunner

from chatlean import __version__
from chatlean.cli import main


def test_help_mentions_tree_option():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "--tree-brief" in result.output


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatlean, version {__version__}" in result.output


def test_tree_reports_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert result.output == (
        "chatlean\n"
        "├── --help  # Show this message and exit.\n"
        "├── --version  # Show the version and exit.\n"
        "├── --tree  # Print the registered CLI tree and exit.\n"
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
    )


def test_tree_brief_reports_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree-brief"])

    assert result.exit_code == 0
    assert result.output == (
        "chatlean\n"
        "├── --help  # Show this message and exit.\n"
        "├── --version  # Show the version and exit.\n"
        "├── --tree  # Print the registered CLI tree and exit.\n"
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
    )
