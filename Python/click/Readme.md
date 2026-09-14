
# Click

**Click** is a Python library used to create command-line interface (CLI) applications easily. It provides decorators and utilities for handling commands, options, arguments, help messages, and user input.

## Installation

```bash
pip install click
```

## Basic Example

```python
import click

@click.command()
@click.option("--name", prompt="Enter your name")
def hello(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    hello()
```

Run:

```bash
python script.py
```

Example output:

```text
Enter your name: Ishan
Hello, Ishan!
```

## Command-Line Arguments

Click can accept arguments directly from the command line.

```python
import click

@click.command()
@click.argument("target")
def scan(target):
    click.echo(f"Scanning target: {target}")

if __name__ == "__main__":
    scan()
```

Run:

```bash
python scan.py example.com
```

Output:

```text
Scanning target: example.com
```

## Options

Options allow users to customize how a command works.

```python
import click

@click.command()
@click.option("--port", default=80, help="Port to scan")
def check(port):
    click.echo(f"Checking port: {port}")

if __name__ == "__main__":
    check()
```

Run:

```bash
python check.py --port 443
```

Output:

```text
Checking port: 443
```

## Multiple Commands

Click can be used to create tools with multiple commands.

```python
import click

@click.group()
def cli():
    """Cybersecurity CLI tool."""
    pass

@cli.command()
@click.argument("target")
def scan(target):
    click.echo(f"Scanning {target}")

@cli.command()
def info():
    click.echo("Security Tool v1.0")

if __name__ == "__main__":
    cli()
```

Run:

```bash
python tool.py scan example.com
```

or:

```bash
python tool.py info
```

## User Input

Click provides simple functions for taking input from users.

```python
import click

name = click.prompt("Enter your name")
click.echo(f"Welcome, {name}")
```

## Password Input

Click can safely hide password input from the terminal.

```python
import click

password = click.prompt(
    "Enter password",
    hide_input=True
)

click.echo("Password received.")
```

> Never print or store passwords unnecessarily in real applications.

## Confirmation

Click can ask the user for confirmation before performing an action.

```python
import click

if click.confirm("Do you want to continue?"):
    click.echo("Continuing...")
else:
    click.echo("Operation cancelled.")
```

## Cybersecurity Use Cases

Click is useful when building cybersecurity command-line tools such as:

* Port scanning tools
* Network enumeration tools
* DNS lookup tools
* Hashing utilities
* File analysis tools
* Log analysis tools
* Vulnerability assessment tools
* URL reconnaissance tools
* Security automation scripts
* Malware analysis utilities

### Example: Simple Security CLI

```python
import click
import socket

@click.command()
@click.argument("domain")
def lookup(domain):
    """Resolve a domain to an IP address."""
    try:
        ip = socket.gethostbyname(domain)
        click.echo(f"Domain : {domain}")
        click.echo(f"IP     : {ip}")
    except socket.gaierror:
        click.echo("Unable to resolve domain.")

if __name__ == "__main__":
    lookup()
```

Run:

```bash
python lookup.py example.com
```

Example output:

```text
Domain : example.com
IP     : 93.184.216.34
```

## Useful Click Features

| Feature                   | Purpose                        |
| ------------------------- | ------------------------------ |
| `@click.command()`        | Creates a CLI command          |
| `@click.group()`          | Creates multiple commands      |
| `@click.argument()`       | Accepts positional arguments   |
| `@click.option()`         | Adds optional parameters       |
| `click.echo()`            | Prints output                  |
| `click.prompt()`          | Gets user input                |
| `click.confirm()`         | Asks for confirmation          |
| `click.password_option()` | Handles password options       |
| `click.Path()`            | Validates file/directory paths |

## Why Use Click?

Click makes Python security tools easier to use from the terminal. Instead of writing complex `input()` and argument-handling code, developers can create clean and structured CLI applications with commands, options, validation, and help messages.

## Learning Goals

In this section, I practiced:

* Creating CLI applications with Click
* Using commands and subcommands
* Handling arguments and options
* Taking user input
* Adding help messages
* Creating security-focused CLI tools
* Combining Click with Python security modules

## Requirements

* Python 3.x
* Click

Install Click with:

```bash
pip install click
```

## References

* [Click Documentation](https://click.palletsprojects.com/)
* [Click PyPI](https://pypi.org/project/click/)

---

**Author:** Ishan Walia
**Focus:** Python & Cybersecurity
