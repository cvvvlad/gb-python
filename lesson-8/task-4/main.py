from devices import Printer, Scaner, MFP
from departments import Department, Storage

storage = Storage()

devices = [
    Printer("HP", "Deskjet 2320"),
    Scaner("Canon", "LiDE300"),
    Scaner("Plustek", "OpticSlim 2700"),
    Scaner("Kodak", "ScanMate i940"),
    MFP("Xerox", "3320DNI")
]

for device in devices:
    storage.add_device(device)

accounting_department = Department("Бухгалтерия")
it_department = Department("IT отдел")
human_resources_department = Department("Отдел кадров")

storage.transfer_device("принтер", accounting_department)
storage.transfer_device("принтер", it_department)
storage.transfer_device("сканер", it_department)
# storage_1.transfer_device("МФУ", human_resources_department)
