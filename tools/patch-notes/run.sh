#!/usr/bin/env bash
# Archive NA/EU official patch notes + GM Notes to research/patch-notes/ (markdown, incremental).
# Uses the Playwright docker container to render the JS-gated official news pages.
# Usage:  tools/patch-notes/run.sh           # last 6 months (default)
#         MONTHS_BACK=12 tools/patch-notes/run.sh
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$DIR/../.." && pwd)"
IMG="mcr.microsoft.com/playwright:v1.60.0-jammy"

docker run --rm --network host \
  --user "$(id -u):$(id -g)" \
  -e HOME="$DIR/.home" \
  -e MONTHS_BACK="${MONTHS_BACK:-6}" \
  -e npm_config_cache="$DIR/.home/.npm" \
  -v "$REPO":"$REPO" -w "$DIR" \
  "$IMG" bash -lc '
    [ -d node_modules/playwright ] || npm i --silent --no-fund --no-audit playwright@1.60.0
    node fetch.mjs
  '
