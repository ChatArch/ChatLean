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

[英文版](README.en.md) | [简体中文](README.md)
</div>

# ChatLean

ChatLean 是 ChatArch 的 Lean tooling 包入口。当前包保持最小 root-only CLI，用于保留可安装、可发现、可发布的 Lean 工具壳；真实 Lean 编排命令尚未暴露。

## 快速开始

```bash
pip install ChatLean
chatlean --help
chatlean --version
chatlean --tree
chatlean --tree-brief
```

## 当前 CLI 树

```text
chatlean
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## CLI 边界

- 当前 CLI 只有根选项，没有业务子命令。
- `--tree` 通过 ChatStyle 共享运行时从实际 Click 注册面生成，并默认保留参数签名；`--tree-brief` 保留命令节点和说明，但省略参数签名。
- 当前 root-only 注册面只有无值 flag，因此两种模式的文本暂时相同；新增带参数的命令后，两种输出会体现签名差异。
- 后续新增真实 Lean 环境、包、证明或执行编排命令时，必须先更新 Click 注册面，再用真实 `chatlean --tree` 和 `chatlean --tree-brief` 同步文档。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：长期维护文档，由 MkDocs 构建

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
