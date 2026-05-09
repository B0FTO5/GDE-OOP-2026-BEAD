from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, plate_number, model, renting_fee):
        self._plate_number = plate_number
        self._model = model
        self._validate_renting_fee(renting_fee)
        self._renting_fee = renting_fee

    @property
    def plate_number(self):
        return self._plate_number

    @property
    def model(self):
        return self._model

    @property
    def renting_fee(self):
        return self._renting_fee

    @abstractmethod
    def __str__(self):
        pass

    def _validate_renting_fee(self, renting_fee):
        if renting_fee <= 0:
            raise ValueError("A bérleti díjnak nagyobbnak kell lennie 0-nál")