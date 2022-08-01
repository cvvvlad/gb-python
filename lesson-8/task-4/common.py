from uuid import uuid4, UUID


class HaveIdMixin:
    """ Базовый класс для всех сущностей у которых есть уникальный идентификатор GUID """
    __id: UUID = None

    @property
    def id(self):
        if self.__id is None:
            self.__id = uuid4()
        return self.__id
