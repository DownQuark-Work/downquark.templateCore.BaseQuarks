# DeepSeek CodeWhale Harness :: Artificial Intelligence Implementation

---

## DeepSeek CodeWhale Harness

> DeepSeek Harness says: everything is a plugin. So DSH itself can be one too.

| Dispatch work, watch progress, collect results, answer its calls for help — one ledger, all inside your codewhale session.

## Overview

> Full Transparency:
> The solution that allow 3 locations to be aware of the same `skills` from a single Implementation was originally created here:
>
> > `https://github.com/zhiyuchen1101/codewhale-dsh/`

However, I will be refactoring and expanding this implementation to make it more modular and reusable.

## Why

DSH ecosystem bridges all point one way (tool → DSH). This project points the other way:

> **DSH → codewhale.** Not a guest UI, not a borrowed toolset — a full agent with its own plugin tree, running alongside yours.

### Full Architecture Overview

```
┌────────────────────────────────────────────────────┐
│ codewhale TUI        your daily · your ledger      │
│        │ MCP (mcp.json)                            │
│        ▼                                           │
│ dsh-bridge            FastMCP thin shell           │
│   tools: dsh_init · dsh_status                     │
│          dsh_read  · dsh_cancel                    │
│   board: task_board.json  (single-writer machine)  │
│        │ spawn                                     │
│        ▼                                           │
│ DSH headless          its own engine & plugins     │
└────────────────────────────────────────────────────┘
```

## How it works

The bridge translates protocols only — no agent logic, no decisions. The board is the single source of truth; the DSH process is the only worker.

### ENV

#### ENVIRONMENT VARIABLES

> Including for completeness
> The following should not need to be changed, but they are somewhat tricky to find.

```
DSH_REPO
DSH_ACP_CONFIG
DSH_ACP_SERVER
DEEPSEEK_API_KEY
```

## Tools

| Tool                        | What it does                                                     |
| --------------------------- | ---------------------------------------------------------------- |
| `dsh_init(task, workspace)` | Dispatch a task. Rejects while busy; resets after `done`/`error` |
| `dsh_status()`              | Poll status; auto-settles `done`/`error` when the process exits  |
| `dsh_read()`                | Read the full result                                             |
| `dsh_respond(allow)`        | Answer a permission/help request (`blocked` state)               |
| `dsh_cancel()`              | Graceful ACP cancel; kill fallback                               |

## Quick start

> ![NOTE]:
> It looks like the `--acp` bug is resolved.
>
> ---
>
> `serve --acp` no longer ignores the approval posture. The ACP adapter
> hardcoded `ApprovalMode::Suggest`, so `--yolo` (and any configured
> `approval_policy`) never reached admission: every mutating tool parked
> behind a permission request no unattended client answers, and sessions
> executed zero tools. Posture now derives from server config — `--yolo`
> pre-approves prompts and flows into the sandbox policy — while hard blocks
> (safety floor, repo law, reviewer consult) and the Plan read-only guardrail
> stay intact (_**#6337**_).

## Installation

### CodeWhale

```sh
# make sure to use version v0.10.0+
curl -fsSL https://codewhale.net/install.sh | CODEWHALE_VERSION="v0.10.0" sh
"$HOME/.local/bin/codewhale" --version
```

> ![Note]:
> To allow mulple instances to be able to be configured and the same time we add a bit more funcitonality to the `make install` command.
> To do that we have already cloned the following git repository:
>
> - `https://github.com/zhiyuchen1101/codewhale-dsh`

This means that all enhancements are already available locally.

- complete the installation with the following

```sh
cd codewhale-dsh
npm install
make install`
```

---

Notice what we have done doing by running:

- `% cat ~/.codewhale/mcp.json`

```sh
{
  "servers": {
    "dsh": {
      "command": "${CODEWHALE_HARNESS_ENABLE_DIRECTORY}.venv/bin/python",
      "args": [ "${CODEWHALE_HARNESS_ENABLE_DIRECTORY}.venv/bin/python}/src/dsh_bridge.py"],
      "env": { "CODEWHALE_HARNESS_ENABLE_DIRECTORY": "./" }
    }
  }
}
```

And by running:

- `% echo $CODEWHALE_HARNESS_ENABLE_DIRECTORY`
- (_output:_ will be the directy `make install` was just run in)

---

## ACTIVATION

> ![TIP]: your life will be easier if all off the following are run from the `codewhale-dsh` directory.'
>
> - Make any new windows and `cd` to the `codewhale-dsh` directory before contining.

Activate the build:

- `% codewhale` :: start codewhale TUI
- `% codewhale serve --acp --yolo` :: start codewhale ACP server
  - periodically check to see if `--yolo` is required as the versioning increases
- Configure `Zed` (or your IDE) to integrate with the ACP server
  - There are too many possibilities for the above step to be written out.
  - You may need to refer to your IDE's documentation.
- `% make bridge` :: this starts the harness and calls `dsh_init` to dispatch a task

## CONGRATS!

- You have successfully activated the build.
