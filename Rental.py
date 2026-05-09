from datetime import datetime, date

class Rental():
    def __init__(self, vehicle, rental_date):
        self._validate_date(rental_date)
        self._vehicle = vehicle
        self._rental_date = rental_date

    @property
    def rental_date(self):
        return self._rental_date

    @property
    def vehicle(self):
        return self._vehicle

    def _validate_date(self, rental_date):
        try:
            parsed_date = datetime.strptime(rental_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Nem megfelelő dátumot formátum.')

        if parsed_date < date.today():
            raise ValueError('A bérlés dátuma nem lehet a múltban')
