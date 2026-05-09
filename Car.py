from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plate_number, model, renting_fee, seat_count, fuel_type):
        super().__init__(plate_number, model, renting_fee)
        self._seat_count = seat_count
        self._fuel_type = fuel_type

    @property
    def seat_count(self):
        return self._seat_count

    @property
    def fuel_type(self):
        return self._fuel_type

    def __str__(self):
        return f"Személyautó - Típus: {self.model}, Rendszám: {self.plate_number}, Ülések száma: {self.seat_count},Üzemanyag típusa: {self.fuel_type}"

    def _validate_seat_count(self, seat_count):
        if seat_count <= 1:
            raise ValueError("Az üléesk számának 1-nél nagyobbnak kell lennie")