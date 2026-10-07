#!/bin/bash
# One-time setup of the GTAlmanac video kit in the current folder.
set -e
# num2words needs docopt; its legacy build fails on some Debian pythons unless built with PEP 517
pip install --break-system-packages -q --use-pep517 docopt 2>/dev/null || true
pip install --break-system-packages -q pocketsphinx num2words 2>/dev/null || pip install -q pocketsphinx num2words
[ -f package.json ] || npm init -y >/dev/null
npm i -s @fontsource/anton @fontsource/inter >/dev/null 2>&1
node -e "try{require('playwright')}catch(e){require(require('child_process').execSync('npm root -g').toString().trim()+'/playwright')}" 2>/dev/null \
  || PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm i -s playwright >/dev/null 2>&1
which ffmpeg ffprobe >/dev/null && echo "setup ok"
