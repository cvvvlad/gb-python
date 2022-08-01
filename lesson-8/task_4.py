from abc import ABC
from uuid import uuid4, UUID


class DevicesRanOutError(Exception):
    """ Ошибка возникающая если на складе закончились устройства """
    pass


class HaveId(ABC):
    """ Базовый класс для всех сущностей у которых есть уникальный идентификатор GUID """
    __id: UUID = None

    @property
    def id(self):
        if self.__id is None:
            self.__id = uuid4()
        return self.__id


class DeviceState:
    off = "off"
    on = "on"


class Device(HaveId):
    _state = DeviceState.off

    def __init__(self, device_type: str, vendor: str, model: str):
        self._device_type = device_type
        self._vendor = vendor
        self._model = model

    def on(self):
        self._state = DeviceState.on

    def off(self):
        self._state = DeviceState.off

    def __str__(self):
        return f"{self._device_type.capitalize()} {self._vendor} {self._model} (id:{self.id}) состояние:{self.state}"

    @property
    def state(self):
        return self._state

    @property
    def device_type(self):
        return self._device_type


class HaveDevices(ABC):
    """ Базовый класс для всех сущностей содержащих устройства"""
    _devices: list[Device] = []

    def add_device(self, device: Device):
        self._devices.append(device)

    def remove_device(self, device_id: UUID):
        for device in self._devices:
            if device.id == device_id:
                self._devices.remove(device)

    def get_devices_by_type(self, device_type: str):
        return [device for device in self._devices if device.device_type.lower().strip() == device_type.lower().strip()]


class Department(HaveDevices, HaveId):
    """ Подразделение компании """

    def __init__(self, name):
        self.name = name


class Storage(HaveDevices, HaveId):
    """ Склад техники """
    __devices_to_departments: dict[UUID, list[UUID]] = {}

    def transfer_device(self, device_type: str, department: Department):
        self.__register_department(department)
        available_devices = self.get_devices_by_type(device_type)
        if not any(available_devices):
            raise DevicesRanOutError()
        device_to_transfer = available_devices[0]
        self.__devices_to_departments[department.id].append(device_to_transfer.id)
        self._devices.remove(device_to_transfer)
        department.add_device(device_to_transfer)
        print(f"{self} передал подразделению {department.name} {device_to_transfer}")

    def __register_department(self, department: Department):
        if not any(key for key in self.__devices_to_departments.keys() if key == department.id):
            self.__devices_to_departments[department.id] = []

    def print_info(self):
        result_str = f"{self}\n"
        for device in self._devices:
            result_str += f"{device}\n"
        return result_str

    def __str__(self):
        return f"Склад (id:{self.id})"


class PrinterState(DeviceState):
    printing = 'printing'


class ScanerState(DeviceState):
    scanning = 'scanning'


class CopierState(DeviceState):
    coping = 'coping'


class Printer(Device):
    """ Принтер """

    def __init__(self, vendor, model):
        super().__init__("принтер", vendor, model)

    def print(self):
        if self._state == PrinterState.off:
            print(f"ОШИБКА! {self} выключен и не может печатать.")
        print(f"{self} печатает")


class Scaner(Device):
    """ Сканер """

    def __init__(self, vendor, model):
        super().__init__("сканер", vendor, model)

    def scan(self):
        if self._state == ScanerState.off:
            print(f"ОШИБКА! {self} выключен и не может печатать.")
        print(f"{self} сканирует")


class MFP(Printer, Scaner):
    """ МФУ - многофункциональное устройство (MFP - Multi-Function Printer) """

    def __init__(self, vendor, model):
        super().__init__(vendor, model)
        self._device_type = 'МФУ'


storage_1 = Storage()

devices = [
    Printer("HP", "Deskjet 2320"),
    Scaner("Canon", "LiDE300"),
    Scaner("Plustek", "OpticSlim 2700"),
    Scaner("Kodak", "ScanMate i940"),
    MFP("Xerox", "3320DNI")
]

for device in devices:
    storage_1.add_device(device)

accounting_department = Department("Бухгалтерия")
it_department = Department("IT отдел")
human_resources_department = Department("Отдел кадров")

storage_1.transfer_device("принтер", accounting_department)
storage_1.transfer_device("принтер", it_department)
storage_1.transfer_device("сканер", it_department)
#storage_1.transfer_device("МФУ", human_resources_department)
