from Car import Car
from Truck import Truck
from Rental import Rental
from CarRental import CarRental
from datetime import datetime

class CarRentalSystem():
    def __init__(self):
        self._car_rental = CarRental("Avis")
        self._init_data()

    def _init_data(self):
        car1 = Car('AAA-123','Yaris', 10000, 4, 'Benzines')
        car2 = Car('BBB-123', 'Corolla', 20000, 4, 'Benzines')
        truck1 = Truck('DDD-123','Volvo', 40000, 5000, 1000)
        self._car_rental.vehicles = car1
        self._car_rental.vehicles = car2
        self._car_rental.vehicles = truck1

        self._car_rental.rentals = Rental(car1, datetime.strptime('2026-06-01', '%Y-%m-%d').date())
        self._car_rental.rentals = Rental(car1, datetime.strptime('2026-06-02', '%Y-%m-%d').date())
        self._car_rental.rentals = Rental(car2, datetime.strptime('2026-06-10', '%Y-%m-%d').date())
        self._car_rental.rentals = Rental(truck1, datetime.strptime('2026-06-01', '%Y-%m-%d').date())

    def user_interact(self):
        while True:
            print('1. Autók listázása')
            print('2. Bérlések listázása')
            print('3. Autó bérlése')
            print('4. Autóbérlés törlése')
            print('5. Kilépés')

            menu = input('Válassz a fenti menüpontokból: ')

            if menu == '1':
                self._car_rental.vehicles
            elif menu == '2':
                self._car_rental.rentals
            elif menu == '3':
                plate_number = input('Add meg a rendszámot: ')
                rental_date_string = input('Add meg bérlés dátumát (ÉÉÉÉ-HH-NN): ')
                rental_date = datetime.strptime(rental_date_string, '%Y-%m-%d').date()
                try:
                    self._car_rental.place_booking(plate_number, rental_date)
                    print(f"A {plate_number} rendszámú autó sikeresen lefoglalva a {rental_date} dátumra.")
                except Exception as e:
                    print(e)
            elif menu == '4':
                plate_number = input('Add meg a rendszámot: ')
                rental_date_string = input('Add meg bérlés dátumát (ÉÉÉÉ-HH-NN): ')
                rental_date = datetime.strptime(rental_date_string, '%Y-%m-%d').date()
                try:
                    self._car_rental.remove_booking(plate_number, rental_date)
                    print(f"A foglalás sikersen törölve.")
                except Exception as e:
                    print(e)
            elif menu == '5':
                break
            else:
                print("Érvénytelen menü")

car_rental_system = CarRentalSystem()
car_rental_system.user_interact()