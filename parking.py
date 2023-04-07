import random

class ParkingLot:
    def __init__(self, size, spot_size=(8, 12)):
        self.size = size
        self.spot_size = spot_size
        self.num_spots = self.size // (spot_size[0] * spot_size[1])
        self.spots = [None] * self.num_spots
        
    def find_empty_spot(self):
        empty_spots = [i for i, spot in enumerate(self.spots) if spot is None]
        if empty_spots:
            return random.choice(empty_spots)
        else:
            return None
        
class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        
    def __str__(self):
        return f"Car with license plate {self.license_plate}"
        
    def park(self, parking_lot, spot_num):
        if parking_lot.spots[spot_num] is None:
            parking_lot.spots[spot_num] = self
            print(f"{self} parked successfully in spot {spot_num}.")
            return True
        else:
            print(f"Spot {spot_num} is occupied. Trying another spot...")
            empty_spot = parking_lot.find_empty_spot()
            if empty_spot is not None:
                return self.park(parking_lot, empty_spot)
            else:
                print("Parking lot is full.")
                return False
            
def main(cars, parking_lot):
    random.shuffle(cars)
    for car in cars:
        empty_spot = parking_lot.find_empty_spot()
        if empty_spot is not None:
            car.park(parking_lot, empty_spot)
        else:
            print("Parking lot is full.")
            break


cars = [Car("ABC1234"), Car("DEF5678"), Car("GHI9101"), Car("JKL2345")]
parking_lot = ParkingLot(2000, spot_size=(10, 12))
main(cars, parking_lot)
