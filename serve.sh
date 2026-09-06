#!/bin/bash
python3 -m venv ~/virtual-envs/mkdocs
source ~/virtual-envs/mkdocs/bin/activate
pip install -r requirements.txt

# Install mermaid-cli for PDF pre-rendering (skip Chromium download, use system Chrome)
if ! command -v mmdc &>/dev/null; then
    echo "Installing @mermaid-js/mermaid-cli..."
    PUPPETEER_SKIP_DOWNLOAD=true npm install -g @mermaid-js/mermaid-cli 2>/dev/null
fi
#mkdocs build
pip list | grep mkdocs
read -p "Press enter to continue"
PRERENDER_MERMAID=1 mkdocs serve
deactivate
