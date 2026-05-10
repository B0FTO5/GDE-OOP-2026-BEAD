from Car import Car
from Truck import Truck
from Rental import Rental
from CarRental import CarRental

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

        # Kivetelkezelés teszteléséhez adunk meg rossz bemeneteket is
        rentals_data = [
            (car1, '2025-06-01'),
            (truck1, '20250601'),
            (car1, '2026-07-01'),
            (car1, '2026-07-02'),
            (car2, '2026-07-10'),
            (truck1, '2026-07-01'),
        ]

        # Elkapjuk a kivételeket, végül csak 4 bérlés fog létrejönni a feladatkiírásnak megfelelően
        for car, rental_date in rentals_data:
            try:
                self._car_rental.rentals = Rental(car, rental_date)
            except Exception as e:
                print(f"Hiba ({car}, {rental_date}): {e}")

        print(f"A {self._car_rental.name} autókölcsönző rendszer inicializálása megtörtént")
        print("*********************************************************************************************************************************\n")

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
                try:
                    self._car_rental.place_booking(plate_number, rental_date_string)
                    print(f"A {plate_number} rendszámú autó sikeresen lefoglalva a {rental_date_string} dátumra.")
                except Exception as e:
                    print(f"Hiba (Megadott rendszám: {plate_number}, Megadott dátum: {rental_date_string}): {e}")
            elif menu == '4':
                plate_number = input('Add meg a rendszámot: ')
                rental_date_string = input('Add meg bérlés dátumát (ÉÉÉÉ-HH-NN): ')
                try:
                    self._car_rental.remove_booking(plate_number, rental_date_string)
                    print(f"A bérlés sikersen törölve.")
                except Exception as e:
                    print(f"Hiba (Megadott rendszám: {plate_number}, Megadott dátum: {rental_date_string}): {e}")
            elif menu == '5':
                break
            else:
                print("Érvénytelen menü")

car_rental_system = CarRentalSystem()
car_rental_system.user_interact()