#!/usr/bin/env bash

set -euo pipefail

# Ensure script is run with root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Error: This script must be run as sudo." >&2
  exit 1
fi

# Get the target directory input (defaults to present working directory)
RAW_DIR="${CODEWHALE_HARNESS_ENABLE_DIRECTORY:-.}"

# Resolve home directory of the original non-root user running sudo
if [ -n "${SUDO_USER:-}" ]; then
  REAL_USER_HOME=$(eval echo "~${SUDO_USER}")
else
  REAL_USER_HOME="$HOME"
fi

# Expand leading tilde `~` manually if provided in CODEWHALE_HARNESS_ENABLE_DIRECTORY
if [[ "$RAW_DIR" == "~"* ]]; then
  RAW_DIR="${REAL_USER_HOME}${RAW_DIR#~}"
fi

# Resolve to an absolute path
if ! TARGET_DIR=$(cd "$RAW_DIR" 2>/dev/null && pwd -P); then
  echo "Error: Directory '$RAW_DIR' does not exist." >&2
  exit 1
fi

# Ensure TARGET_DIR has a trailing slash for clean path concatenation
[[ "$TARGET_DIR" != */ ]] && TARGET_DIR="${TARGET_DIR}/"

CONFIG_FILE="${REAL_USER_HOME}/.codewhale/mcp.json"

if [ ! -f "$CONFIG_FILE" ]; then
  echo "Error: Configuration file not found at $CONFIG_FILE" >&2
  exit 1
fi

# Modify JSON in-place via embedded Python
python3 - "$CONFIG_FILE" "$TARGET_DIR" << 'EOF'
import json
import sys
import re

config_path = sys.argv[1]
target_dir = sys.argv[2]

with open(config_path, 'r') as f:
    content = f.read()

# Sanitize trailing commas if present in source file
content_cleaned = re.sub(r',(\s*[}\]])', r'\1', content)

try:
    data = json.loads(content_cleaned)
except json.JSONDecodeError as e:
    sys.exit(f"Failed to parse JSON in {config_path}: {e}")

if "servers" not in data:
    data["servers"] = {}

# Ensure 'dsh' object exists without overwriting existing fields (like 'url' or 'connect_timeout')
if "dsh" not in data or not isinstance(data["dsh"], dict):
    data["dsh"] = {
        "url": None,
        "connect_timeout": 1234
    }

# Update ONLY the specified fields with absolute paths
data["dsh"]["command"] = f"{target_dir}.venv/bin/python"
data["dsh"]["args"] = [f"{target_dir}src/dsh_bridge.py"]
data["dsh"]["env"] = {"CODEWHALE_HARNESS_ENABLE_DIRECTORY": target_dir}

with open(config_path, 'w') as f:
    json.dump(data, f, indent=2)
    f.write('\n')

EOF

echo "Successfully updated 'dsh' in $CONFIG_FILE"
echo "Resolved Absolute Path: $TARGET_DIR"
