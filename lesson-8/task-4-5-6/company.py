from departments import Storage, Department
from devices import Printer, Scaner, MFP


class Company:

    def __init__(self):
        self.storage = Storage()
        self.__departments: list[Department] = []
        self.seed_test_data()

    def seed_test_data(self):
        self.__departments = [
            Department("Бухгалтерия"),
            Department("IT отдел"),
            Department("Отдел кадров")
        ]

        devices = [
            Printer("HP", "Deskjet 2320"),
            Scaner("Canon", "LiDE300"),
            Scaner("Plustek", "OpticSlim 2700"),
            Scaner("Kodak", "ScanMate i940"),
            MFP("Xerox", "3320DNI")
        ]
        for device in devices:
            self.storage.add_device(device)

    def add_department(self, name):
        new_department = Department(name)
        self.__departments.append(new_department)
        return new_department

    def get_department_by_id(self, department_id: int):
        found_departments = [dep for dep in self.departments if dep.id == department_id]
        return found_departments[0] if found_departments else None

    @property
    def departments(self):
        return sorted(self.__departments, key=lambda d: d.id)
