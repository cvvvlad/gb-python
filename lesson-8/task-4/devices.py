from common import HaveIdMixin
from uuid import UUID
from abc import ABC


class DeviceState:
    off = "off"
    on = "on"


class Device(HaveIdMixin):
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


class PrinterState(DeviceState):
    printing = 'printing'


class Printer(Device):
    """ Принтер """

    def __init__(self, vendor, model):
        super().__init__("принтер", vendor, model)

    def print(self):
        if self._state == PrinterState.off:
            print(f"ОШИБКА! {self} выключен и не может печатать.")
        print(f"{self} печатает")


class ScanerState(DeviceState):
    scanning = 'scanning'


class Scaner(Device):
    """ Сканер """

    def __init__(self, vendor, model):
        super().__init__("сканер", vendor, model)

    def scan(self):
        if self._state == ScanerState.off:
            print(f"ОШИБКА! {self} выключен и не может печатать.")
        print(f"{self} сканирует")


class MFPState(PrinterState, ScanerState):
    pass


class MFP(Printer, Scaner):
    """ МФУ - многофункциональное устройство (MFP - Multi-Function Printer) """

    def __init__(self, vendor, model):
        super().__init__(vendor, model)
        self._device_type = 'МФУ'
