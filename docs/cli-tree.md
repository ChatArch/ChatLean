# CLI 树

`ChatLean` 当前是 root-only CLI。这个页面必须从真实 `chatlean --tree` 和 `chatlean --tree-brief` 输出同步，不能手写未来命令。

```text
chatlean
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`--tree` 通过 ChatStyle 共享运行时默认保留参数签名；`--tree-brief` 保留命令节点和说明，但省略参数签名。当前 root-only 注册面只有无值 flag，因此两种输出暂时相同。

## 当前状态

| 入口 | 状态 | 说明 |
| --- | --- | --- |
| `chatlean --help` | 已实现 | 显示根命令帮助。 |
| `chatlean --version` | 已实现 | 显示已安装包版本。 |
| `chatlean --tree` | 已实现 | 显示带参数签名的当前真实 CLI 树。 |
| `chatlean --tree-brief` | 已实现 | 显示省略参数签名的当前真实 CLI 树。 |
| Lean 工具子命令 | 尚未实现 | 未来有实际 Lean 编排能力后再加入 CLI。 |

## 更新规则

新增真实命令时，先更新 Click 注册面和测试，再运行 `chatlean --tree` 与 `chatlean --tree-brief` 回填 README 与本页。
