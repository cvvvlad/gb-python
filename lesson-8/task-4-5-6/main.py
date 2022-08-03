from console_helpers import HelpCommand, ConsoleCommand, NewCommand, ShowCommand, TransferCommand
from rich.console import Console
from rich.prompt import Prompt
from company import Company

console = Console()
company = Company()

help_command = HelpCommand(console, company)
available_commands: list[ConsoleCommand] = [
    help_command,
    NewCommand(console, company),
    ShowCommand(console, company),
    TransferCommand(console, company)
]
help_command.available_commands = available_commands

console.print("[bold]Добро пожаловать в [cyan]МенеджерСклада Rolyal Deluxe Professinal Plus LTS")
console.print(f"Для вывода справки по программе введите [bold green]{help_command.keyword}")

while True:
    input_str = Prompt.ask()
    parts = input_str.split(' ')
    keyword = parts[0].strip().lower()
    for command in available_commands:
        if command.keyword == keyword:
            command_args = parts[1:]
            command.execute(command_args)
