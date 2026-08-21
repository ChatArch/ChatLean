# Changelog

## 2026-08-21 - 0.1.3

### Changed

- Migrated the canonical `chatlean` Click tree to `chatstyle.add_tree_option`, with detailed `--tree` and signature-free `--tree-brief` views.
- Updated the supported runtimes to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.

## 2026-08-12 - 0.1.2

### Added

- Added real root-only `chatlean --tree` generated from the Click command surface.
- Added bilingual MkDocs home and CLI tree pages.
- Added CLI and workflow/docs contract tests.

### Changed

- Aligned documentation URL to `https://arch.gh.wzhecnu.cn/ChatLean/`.
- Hardened CI, Preview Docs, Deploy Docs, and tag-only OIDC publish workflows.

## 2026-07-01 - 0.1.1

### Changed

- Prepare continuous Publisher-backed patch release for ChatLean.

## 2026-06-29 - 0.1.0

### Added

- Initial ChatLean package scaffold with `chatlean` CLI.
- ChatEnv provider entry point for `chatlean` configuration discovery.
- CI and tag-driven publish workflow scaffold.
