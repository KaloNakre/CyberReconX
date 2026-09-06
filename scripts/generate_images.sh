#!/usr/bin/env bash
set -euo pipefail

# Example helper to generate images using Automatic1111 web UI's REST API.
# Requires: Automatic1111 stable-diffusion-webui running on localhost:7860
# Usage: ./generate_images.sh "Cyberpunk prompt text" out.png

PROMPT=${1:-""}
OUT=${2:-out.png}

if [ -z "$PROMPT" ]; then
  echo "Usage: $0 \"Prompt text\" output.png"
  exit 1
fi

curl -s -X POST "http://127.0.0.1:7860/sdapi/v1/txt2img" \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"$PROMPT\", \"steps\": 28, \"width\": 1024, \"height\": 576}" \
  -o /tmp/sd_out.json

# The API returns images as base64 inside JSON; extract using jq and base64
if command -v jq >/dev/null 2>&1; then
  IMG_B64=$(jq -r '.images[0]' /tmp/sd_out.json)
  echo "$IMG_B64" | base64 -d > "$OUT"
  echo "Saved $OUT"
else
  echo "jq not installed — output JSON saved to /tmp/sd_out.json"
fi
