# Journal CLI

A simple command-line journaling application built with Python and SQLite.

## About

This project was created as a practice exercise to work with SQLite and Python. It's a basic journaling tool that allows users to add, view, edit, and delete journal entries from the command line.

The project is inspired by [jrnl](https://jrnl.sh), which is a much more comprehensive and feature-rich journaling tool. If you're looking for a more robust solution, I highly recommend checking out jrnl.

## Features

- Add journal entries
- View entries (with options to show IDs and timestamps)
- Edit existing entries
- Delete entries
- Colorized output for improved readability

## Installation

To avoid conflicts with system Python installations, it's recommended to install Journal CLI in a virtual environment or use `pipx` for isolated installation.

### Option 1: Install with pipx (Recommended for general use)

1. Install pipx:
   - On macOS:
     ```
     brew install pipx
     pipx ensurepath
     ```
   - On Linux:
     ```
     python3 -m pip install --user pipx
     python3 -m pipx ensurepath
     ```

2. Install Journal CLI:
   ```
   pipx install git+https://github.com/taylormichaelhall/journal-cli.git
   ```

### Option 2: Install in a virtual environment

1. Create and activate a virtual environment:
   ```
   python3 -m venv journalcli-env
   source journalcli-env/bin/activate
   ```

2. Install Journal CLI:
   ```
   pip install git+https://github.com/taylormichaelhall/journal-cli.git
   ```


You'll need to activate the venv whenever you want to run this in a shell.

### For development:

1. Clone this repository:
   ```
   git clone https://github.com/taylormichaelhall/journal-cli.git
   cd journal-cli
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the package in editable mode:
   ```
   pip install -e .
   ```

## Uninstallation

- If installed with pipx:
  ```
  pipx uninstall journal-cli
  ```

- If installed in a virtual environment:
  ```
  pip uninstall journal-cli
  ```

- To remove the journal database, delete it from your user's home folder in `~/.journal-cli/journal.db`

## Usage

After installation, you can use the `journal-cli` command from anywhere:

- Show help:
  ```
  journal-cli --help
  ```

- Add an entry:
  ```
  journal-cli add Your journal entry goes here
  ```

- Show entries:
  ```
  journal-cli show
  journal-cli show -i  # Show with IDs
  journal-cli show -t  # Show with timestamps
  journal-cli show -i -t  # Show with both IDs and timestamps
  ```

- Edit an entry:
  ```
  journal-cli edit <entry-id> Your updated journal entry
  ```

- Delete an entry:
  ```
  journal-cli delete <entry-id>
  ```

Note: If you installed in a virtual environment, make sure to activate it before using the `journal-cli` command.

## Acknowledgements

- Inspired by [jrnl](https://jrnl.sh)
- Built with Python and SQLite
- Uses [colorama](https://pypi.org/project/colorama/) for colored terminal output