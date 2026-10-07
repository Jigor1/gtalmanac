#!/bin/bash
# One-time setup of the GTAlmanac video kit in the current folder.
set -e
pip install --break-system-packages -q pocketsphinx num2words 2>/dev/null || pip install -q pocketsphinx num2words
[ -f package.json ] || npm init -y >/dev/null
npm i -s @fontsource/anton @fontsource/inter >/dev/null 2>&1
node -e "try{require('playwright')}catch(e){require(require('child_process').execSync('npm root -g').toString().trim()+'/playwright')}" 2>/dev/null \
  || PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm i -s playwright >/dev/null 2>&1
which ffmpeg ffprobe >/dev/null && echo "setup ok"
