<div align="center">
    <a href="https://pypi.python.org/pypi/ChatLean">
        <img src="https://img.shields.io/pypi/v/ChatLean.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatLean/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatLean/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatLean/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatLean

ChatLean is the ChatArch Lean tooling package entrypoint. The package currently keeps a minimal root-only CLI so the Lean tooling shell remains installable, discoverable, and releasable; real Lean orchestration commands are not exposed yet.

## Quick Start

```bash
pip install ChatLean
chatlean --help
chatlean --version
chatlean --tree
chatlean --tree-brief
```

## Current CLI Tree

```text
chatlean
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## CLI Boundary

- The current CLI only exposes root options and has no business subcommands.
- `--tree` is generated from the real Click registration by the shared ChatStyle runtime and retains parameter signatures by default; `--tree-brief` keeps command nodes and descriptions while omitting parameter signatures.
- The current root-only surface contains only value-free flags, so both modes are textually identical for now; parameterized commands will make the signature difference visible.
- When real Lean environment, package, proof, or execution orchestration commands are added later, update the Click registration first and then sync docs from the real `chatlean --tree` and `chatlean --tree-brief` outputs.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by MkDocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
