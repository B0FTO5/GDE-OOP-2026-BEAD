from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, plate_number, model, renting_fee, load_capacity, cargo_volume):
        super().__init__(plate_number, model, renting_fee)
        self._load_capacity = load_capacity
        self._cargo_volume = cargo_volume

    @property
    def load_capacity(self):
        return self._load_capacity

    @property
    def cargo_volume(self):
        return self._cargo_volume

    def __str__(self):
        return f"Teherautó - Típus: {self.model}, Rendszám: {self.plate_number}, Teherbírás: {self.load_capacity} KG, Raktér méret: {self.cargo_volume} m³"
