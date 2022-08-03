import time

from abc import ABC, abstractmethod


class DeviceState:
    off = "выключено"
    on = "включено"


class Device:
    __number: int = None
    __staticIdCounter = 0
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
        return f"{self._device_type.capitalize()} {self._vendor} {self._model}"

    @property
    def id(self):
        if self.__number is None:
            Device.__staticIdCounter += 1
            self.__number = self.__class__.__staticIdCounter
        return self.__number

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def vendor(self):
        return f"{self._vendor}"

    @property
    def model(self):
        return f"{self._model}"

    @property
    def full_name(self):
        return f"{self._device_type.capitalize()} {self._vendor} {self._model}"

    @property
    def device_type(self):
        return self._device_type


class CanPrint(ABC):

    @abstractmethod
    def print(self):
        pass


class CanScan(ABC):

    @abstractmethod
    def scan(self):
        pass


class SimplePrintBehaviour:
    """ Способность печатать """

    def __init__(self, device: Device):
        self.__device = device

    def print(self):
        if self.__device.state == PrinterState.off:
            print(f"ОШИБКА! {self.__device} выключен и не может печатать.")
        previous_state = self.__device.state
        self.__device.state = PrinterState.printing
        print(f"{self} печатает...")
        time.sleep(2)
        print(f"{self} готово")
        self.__device.state = previous_state


class SimpleScanBehaviour:
    """ Способность сканировать"""

    def __init__(self, device: Device):
        self.__device = device

    def scan(self):
        if self.__device.state == ScanerState.off:
            print(f"ОШИБКА! {self.__device} выключен и не может печатать.")
        previous_state = self.__device.state
        self.__device.state = ScanerState.scanning
        time.sleep(3)
        self.__device.state = previous_state


class PrinterState(DeviceState):
    printing = 'печатает'


class ScanerState(DeviceState):
    scanning = 'сканирует'


class MFPState(PrinterState, ScanerState):
    pass


class Printer(Device, CanPrint):
    """Принтер"""

    def __init__(self, vendor, model):
        super().__init__("принтер", vendor, model)
        self.__print_behaviour = SimplePrintBehaviour(self)

    def print(self):
        self.__print_behaviour.print()


class Scaner(Device, CanScan):
    """ Сканер """

    def __init__(self, vendor, model):
        super().__init__("сканер", vendor, model)
        self.__scan_behaviour = SimpleScanBehaviour(self)

    def scan(self):
        self.__scan_behaviour.scan()


class MFP(Device, CanPrint, CanScan):
    """ МФУ - многофункциональное устройство (MFP - Multi-Function Printer) """

    def __init__(self, vendor, model):
        super().__init__('МФУ', vendor, model)
        self.__print_behaviour = SimplePrintBehaviour(self)
        self.__scan_behaviour = SimpleScanBehaviour(self)

    def print(self):
        self.__print_behaviour.print()

    def scan(self):
        self.__scan_behaviour.scan()
