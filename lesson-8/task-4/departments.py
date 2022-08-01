from common import HaveIdMixin
from devices import Device
from uuid import UUID


class HaveDevicesMixin:
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


class Department(HaveDevicesMixin, HaveIdMixin):
    """ Подразделение компании """

    def __init__(self, name):
        self.name = name


class DevicesRanOutError(Exception):
    """ Ошибка возникающая если на складе закончились устройства """
    pass


class Storage(HaveDevicesMixin, HaveIdMixin):
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
