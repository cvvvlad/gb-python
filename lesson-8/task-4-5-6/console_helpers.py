from abc import ABC, abstractmethod
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from rich.tree import Tree
from company import Company
from devices import Device, Printer, Scaner, MFP


def translate_device_type(device_type_eng: str) -> str:
    if device_type_eng == 'printer':
        return 'принтер'
    elif device_type_eng == 'scaner':
        return 'сканер'
    elif device_type_eng == 'mfp':
        return 'МФУ'
    else:
        return ''


def create_devices_table(devices: list[Device], title='Устройства'):
    table = Table(show_header=True, header_style="bold magenta", show_lines=True)
    table.title = f"[bold]{title}[/bold]"
    table.add_column("ID")
    table.add_column("Тип")
    table.add_column("Производитель")
    table.add_column("Модель")
    table.add_column("Состояние")
    for device in devices:
        table.add_row(str(device.id), device.device_type, device.vendor, f"{device.model}", device.state)
    return table


def create_departments_table(company: Company):
    table = Table(show_header=True, header_style="bold magenta", show_lines=True)
    table.title = f"[bold]Подразделения[/bold]"
    table.add_column('ID')
    table.add_column("Название")
    for dep in company.departments:
        table.add_row(str(dep.id), f"[bold]{dep.name}[/bold]")
    return table


def create_company_tree(company: Company):
    tree = Tree("[bold]Компания[/bold]")
    storage_tree = tree.add(f'[bold]{company.storage}')
    for device in company.storage.devices:
        storage_tree.add(f'{device}')
    for dep in company.departments:
        department_tree = tree.add(f"[bold]{dep}[/bold]")
        for device in dep.devices:
            department_tree.add(f'{device}')
    return tree


def create_help_table(available_commands):
    table = Table(show_header=True, header_style="bold magenta", show_lines=True)
    table.title = f"[bold]Список доступных команд[/bold]"
    table.add_column("Команда")
    table.add_column("Описание")
    table.add_column("Пример")
    for command in available_commands:
        table.add_row(command.keyword, command.description, command.example)
    return table


def get_param(args, index, to: int | str = 0):
    result = args[index] if args and len(args) > index else ''

    if to == 'end':
        to = len(args) - 1

    if to != 0:
        for i in range(index + 1, to + 1):
            result += ' ' + args[i]
    return result


def get_int_param(args, index, to: int | str = 0):
    found_str = get_param(args, index, to)
    return int(found_str) if found_str.isnumeric() else None


class ConsoleCommand(ABC):

    def __init__(self, console: Console, company: Company, keyword: str, description: str = '', example: str = ''):
        self.keyword = keyword
        self.description = description
        self.console = console
        self.company = company
        self.example = example

    @abstractmethod
    def execute(self, args):
        pass

    def print_error(self, msg: str):
        self.console.print(f"[red]{msg}[/red]")

    def print_success(self, msg: str):
        self.console.print(f"[green]{msg}[/green]")


class HelpCommand(ConsoleCommand):
    available_commands: list[ConsoleCommand] = []

    def __init__(self, console, company):
        super().__init__(console, company, "?", "Вывод справки")

    def execute(self, *args):
        self.console.print(create_help_table(self.available_commands))


class NewCommand(ConsoleCommand):

    def __init__(self, console, company):
        super().__init__(console, company,
                         keyword="new",
                         description="Создает новый элемент\n"
                                     "Создание устройства: new device [тип устройства] [производитель] [модель]\n"
                                     "Параметры:\n"
                                     "[тип устройства] - [magenta]printer/scaner/mfp[/magenta]\n"
                                     "[производитель] - любой, одним словом\n"
                                     "[модель] - любой набор слов\n"
                                     "[cyan]или[/cyan] new department [название подразделения]",
                         example=":new device printer HP Deskjet 2320\n"
                                 ":new department бухгалтерия")

    def execute(self, args):
        entity_type = get_param(args, 0)
        if not entity_type:
            entity_type = Prompt.ask("Введите тип сущности", choices=["device", "department"]).lower().strip()

        if entity_type == 'device':
            self.new_device(args[1:])
        elif entity_type == 'department':
            self.new_department(args[1:])

    def new_device(self, args):
        device_type = get_param(args, 0)
        vendor = get_param(args, 1)
        model = get_param(args, 2, to='end')

        if not device_type:
            device_type = Prompt.ask("Тип устройства", choices=['printer', 'scaner', 'mfp'])

        if not vendor:
            vendor = Prompt.ask("Производитель")

        if not model:
            model = Prompt.ask("Модель")

        device: Device

        if device_type == 'printer':
            device = Printer(vendor, model)
        elif device_type == 'scaner':
            device = Scaner(vendor, model)
        elif device_type == 'mfp':
            device = MFP(vendor, model)
        else:
            self.print_error("Не верный тип устройства!")
            return

        if device:
            self.company.storage.add_device(device)
        else:
            self.print_error("Не удалось добавить устройство!")
            return

        self.print_success(f"Устройство {device} успешно добавлено на склад!")

    def new_department(self, args):
        department_name = get_param(args, 0)
        if not department_name:
            self.print_error("Не указано название подразделения!")
        new_department = self.company.add_department(department_name)
        self.print_success(f"Подразделение {new_department} добавлено.")


class ShowCommand(ConsoleCommand):
    def __init__(self, console, company):
        super().__init__(console, company,
                         keyword="show",
                         description="Отображает состояние склада/подразделения.\n"
                                     "Синтаксис:\n"
                                     "show [magenta]\[storage/departments/all][/magenta]",
                         example='show all')

    def execute(self, args):
        entity_type = args[0] if args else ''
        self.show(entity_type)

    def process_entity_type(self, entity_type):
        if entity_type == 'storage':
            self.show_storage()
        elif entity_type == 'departments':
            self.show_departments()
        elif entity_type == 'all':
            self.show_all()

    def show(self, entity_type=''):
        if not entity_type:
            entity_type = Prompt.ask("Введите тип сущности", choices=['storage', 'departments', 'all']).lower().strip()
        self.process_entity_type(entity_type)

    def show_storage(self):
        storage = self.company.storage
        self.console.print(create_devices_table(storage.devices, title=f'{storage}'))
        printers_count = storage.get_devices_count("принтер")
        scaner_count = storage.get_devices_count("сканер")
        mfp_count = storage.get_devices_count("МФУ")
        self.console.print(f"Принтеров - {printers_count}, Сканеров - {scaner_count}, МФУ - {mfp_count}")

    def show_departments(self):
        self.console.print(create_departments_table(self.company))

    def show_all(self):
        self.console.print(create_company_tree(self.company))


class TransferCommand(ConsoleCommand):

    def __init__(self, console, company):
        super().__init__(console, company, 'transfer',
                         'Перемещает устройства из со склада в подразделение.\n '
                         'Синтаксис: transfer [тип устройства] [номер подразделения]',
                         'transfer принтер 3')

    def execute(self, args):
        device_type = get_param(args, 0)
        department_id = get_int_param(args, 1)

        if not device_type:
            device_type = Prompt.ask("Тип устройства", choices=['printer', "scaner", "mfp"])

        if not department_id:
            self.console.print(create_departments_table(self.company))
            department_id_str = Prompt.ask("Номер подразделения", choices=[f"{d.id}" for d in self.company.departments])
            department_id = get_int_param([department_id_str], 0)

        target_department = self.company.get_department_by_id(department_id)
        if not target_department:
            self.print_error(f"Не удалось найти подразделение с id={department_id}!")
        transferred_device = self.company.storage.transfer_device(translate_device_type(device_type), target_department)
        self.print_success(f"{transferred_device} успешно передано в {target_department}!")
