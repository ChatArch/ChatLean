# CLI Tree

`ChatLean` is currently a root-only CLI. This page must stay synchronized from the real `chatlean --tree` and `chatlean --tree-brief` outputs and must not invent future commands.

```text
chatlean
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

The shared ChatStyle runtime retains parameter signatures for `--tree` by default; `--tree-brief` keeps command nodes and descriptions while omitting parameter signatures. The current root-only surface contains only value-free flags, so both outputs are textually identical for now.

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatlean --help` | Implemented | Shows root command help. |
| `chatlean --version` | Implemented | Shows the installed package version. |
| `chatlean --tree` | Implemented | Shows the current real CLI tree with parameter signatures. |
| `chatlean --tree-brief` | Implemented | Shows the current real CLI tree without parameter signatures. |
| Lean tooling subcommands | Not implemented | Add them only after real Lean orchestration capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatlean --tree` and `chatlean --tree-brief` to refresh README and this page.
