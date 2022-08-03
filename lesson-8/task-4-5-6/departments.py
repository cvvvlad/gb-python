from devices import Device


class Department:
    """ Подразделение компании """
    __number: int = None
    __staticIdCounter = 0

    def __init__(self, name):
        self.name = name
        self.__devices: list[Device] = []

    def add_device(self, device: Device):
        self.__devices.append(device)

    def __str__(self):
        return f'{self.name}'

    @property
    def devices(self):
        return self.__devices

    @property
    def id(self):
        if self.__number is None:
            Department.__staticIdCounter += 1
            self.__number = self.__class__.__staticIdCounter
        return self.__number


class DevicesRanOutError(Exception):
    """ Ошибка возникающая если на складе закончились устройства """
    pass


class Storage:
    """ Склад техники """

    __number: int = None
    __staticIdCounter = 0
    __devices_to_departments: dict[int, list[int]] = {}
    __devices: list[Device] = []

    def add_device(self, device: Device):
        self.__devices.append(device)

    def transfer_device(self, device_type: str, department: Department):
        self.__register_department(department)
        available_devices = self.get_devices_by_type(device_type)
        if not any(available_devices):
            raise DevicesRanOutError()
        device_to_transfer = available_devices[0]
        self.__devices_to_departments[department.id].append(device_to_transfer.id)
        self.__devices.remove(device_to_transfer)
        department.add_device(device_to_transfer)
        return device_to_transfer

    def __register_department(self, department: Department):
        if not any(key for key in self.__devices_to_departments.keys() if key == department.id):
            self.__devices_to_departments[department.id] = []

    def get_devices_by_type(self, device_type: str):
        return [device for device in self.__devices if
                device.device_type.lower().strip() == device_type.lower().strip()]

    def __str__(self):
        return f"Склад №{self.id}"

    @property
    def devices(self):
        return self.__devices

    @property
    def id(self):
        if self.__number is None:
            Storage.__staticIdCounter += 1
            self.__number = self.__class__.__staticIdCounter
        return self.__number

    def get_devices_count(self, device_type: str):
        return len(self.get_devices_by_type(device_type))
