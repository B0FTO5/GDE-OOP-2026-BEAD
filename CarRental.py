from Rental import Rental
from datetime import datetime

class CarRental:
    def __init__(self, name):
        self._name = name
        self._vehicles = []
        self._rentals = []

    @property
    def name(self):
        return self._name

    @property
    def vehicles(self):
        for vehicle in self._vehicles:
            print(f"{vehicle} - Ár: {vehicle.renting_fee} HUF")

    @property
    def rentals(self):
        for rental in self._rentals:
            print(f"Rendszám: {rental.vehicle.plate_number}, Dátum: {rental.rental_date}, Ár: {rental.vehicle.renting_fee} HUF")

    @vehicles.setter
    def vehicles(self, new_vehicle):
        self._vehicles.append(new_vehicle)

    @rentals.setter
    def rentals(self, new_rental):
        self._rentals.append(new_rental)

    def _find_vehicle(self, plate_number):
        for vehicle in self._vehicles:
            if vehicle.plate_number == plate_number:
                return vehicle
        return None

    def _find_rental(self, plate_number, rental_date):
        for rental in self._rentals:
            if (rental.vehicle.plate_number == plate_number and rental.rental_date == rental_date):
                return rental
        return None

    def is_vehicle_booked(self, plate_number, rental_date):
        rental = self._find_rental(plate_number, rental_date)
        return rental is not None

    def place_booking(self, plate_number, rental_date):
        vehicle = self._find_vehicle(plate_number)
        if vehicle is None:
            raise ValueError("A megadott jármű nem létezik")

        if self.is_vehicle_booked(plate_number, rental_date):
            raise Exception("A jármű már foglalt a megadott napon")

        rental = Rental(vehicle, rental_date)
        self._rentals.append(rental)

    def remove_booking(self, plate_number, rental_date):
        try:
            datetime.strptime(rental_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Nem megfelelő dátum formátum.')
        rental = self._find_rental(plate_number, rental_date)
        if rental is None:
            raise ValueError("A megadott foglalás nem létezik.")
        self._rentals.remove(rental)
        return True