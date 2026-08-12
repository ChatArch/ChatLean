# CLI Tree

`ChatLean` is currently a root-only CLI. This page must stay synchronized from the real `chatlean --tree` output and must not invent future commands.

```text
chatlean  # ChatArch Lean tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatlean --help` | Implemented | Shows root command help. |
| `chatlean --version` | Implemented | Shows the installed package version. |
| `chatlean --tree` | Implemented | Shows the current real CLI tree. |
| Lean tooling subcommands | Not implemented | Add them only after real Lean orchestration capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatlean --tree` to refresh README and this page.
