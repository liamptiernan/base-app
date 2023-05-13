# base-app

# Development Setup

Supporting:

- MacOS M1 and Intel

## Pre-reqs

Before we get to app setup and running. You will need these:

- os base packages (varies by OS)
- Docker
- pyenv
- python
- poetry
- nvm
- node
- yarn

### MacOS setup

```sh

# Install base packages

xcode-select --install

# brew is apt more or less
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install gnupg coreutils awscli protobuf libmagic swig xpdf antiword tesseract postgresql

# Install Poetry

curl -sSL https://install.python-poetry.org | python3
export PATH="$HOME/.local/bin:$PATH"
poetry config virtualenvs.in-project true

# poetry install python deps
poetry install

# activating venv
. .venv/bin/activate

```

## Running the services

Each service should run in it's own terminal.

```bash
# Webserver
source .venv/bin/activate
python backend/api/main.py
```
