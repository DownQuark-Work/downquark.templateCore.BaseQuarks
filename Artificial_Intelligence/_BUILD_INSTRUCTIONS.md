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

## Installation (First Run)

### CodeWhale

```sh
# make sure to use version v0.10.0+
curl -fsSL https://codewhale.net/install.sh | CODEWHALE_VERSION="v0.10.0" sh
# or `/Users/<user-name>/<install_location>/codewhale update ` # if you already have it installed
"$HOME/.local/bin/codewhale" --version
```

clone the git repository making sure to replace `<PROJECT_NAME>` with the name you want to give to the project.
And may as well remove their `.git` directory before we run into any issues.

- `git clone https://github.com/zhiyuchen1101/codewhale-dsh <PROJECT_NAME> && cd <PROJECT_NAME> && rm -rf .git*`

The cloned repository gives us access to the:

- DeepSeek harness
- "backwards bridge"
  - this is what allows us to stay focused on the TUI and emit & trigger events _downwards_ to both the DeepSeek harness and the ACP.

When in a directory that is different from the the location that you previously worked on with CodeWhale we need to update the `mcp.json` linking the project root to CodeWhale.

A helper script is provided.
From the project root directory run:

- `% sudo ./update_mcp.sh`

You can verify the settings took effect with:

- `% cat ~/.codewhale/mcp.json`

And you should see a snippet similar to the following:

```sh
{
  "servers": {
    "dsh": {
      "command": "<ABSOLUTE_PROJECT_PATH>.venv/bin/python",
      "args": [ "<ABSOLUTE_PROJECT_PATH>/src/dsh_bridge.py"],
      "env": { "<ABSOLUTE_PROJECT_PATH>/" }
    }
  }
}
```

Complete the installation by running the following from the _Project Root_:

- `% make install`

---

## ACTIVATION

> ![TIP]: your life will be easier if all off the following are run from the `codewhale-dsh` directory.'
>
> - Make any new windows and `cd` to the `codewhale-dsh` directory before contining.

Activate the build from the _Project Root_:

- `% make bridge` :: this starts the MCP for the harness as well as the ACP server
- Configure `Zed` (or your IDE) to integrate with the ACP
  - There are too many possibilities for the above step to be written out.
  - You may need to refer to your IDE's documentation.
- From a non-active terminal start the TUI by running:
  - `% codewhale`

(The values set in `mcp.json` are used to map and persist the TUI to the MCP server active for the current project)

## CONGRATS!

- You have successfully activated the build.
