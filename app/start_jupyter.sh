#!/usr/bin/env bash
# Sobe o Jupyter Notebook com o ambiente do projeto, na pasta do trabalho.
cd "$(dirname "$0")"
exec .venv/bin/python -m notebook --notebook-dir="$(pwd)" --port=8888 --no-browser "$@"
