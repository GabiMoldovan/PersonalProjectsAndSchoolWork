'''
Problema:
Implementeaza un sistem pentru gestionarea diferitelor tipuri de vehicule (de exemplu, masina si camion).
Acest sistem trebuie sa respecte principiile OOP, iar fiecare principiu sa fie reflectat intr-o anumita parte a rezolvarii:

Encapsulare: Asigura-te ca proprietatile fiecarui vehicul (cum ar fi viteza si capacitatea de combustibil) sunt protejate, permitand accesul la ele doar prin metode publice.
Mostenire: Creeaza o clasa de baza generala numita Vehicul, iar clasele derivate Masina si Camion sa mosteneasca din aceasta.
Polimorfism: Metoda accelereaza() trebuie sa se comporte diferit pentru Masina si Camion.
Abstractie: Creeaza o metoda abstracta descriere() in clasa Vehicul, care trebuie implementata in clasele derivate.

'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, speed: float, fuelCapacity: float):
        # incapsulation - protected atributes
        self._speed = speed
        self._fuelCapacity = fuelCapacity

    def getSpeed(self) -> float:
        return self._speed

    def setSpeed(self, newSpeed: float) -> None:
        self._speed = newSpeed

    def getFuelCapacity(self) -> float:
        return self._fuelCapacity

    def setFuelCapacity(self, newFuelCapacity: float):
        self._fuelCapacity = newFuelCapacity

    def accelerate(self, accelerationSpeed: float) -> None:
        print(f"The vehicle is running at {self._speed}, and accelerates at {self._speed + accelerationSpeed}")

    def decelerate(self, decelerationSpeed: float) -> None:
        print(f"The vehicle is running at {self._speed}, and decelerates at {self._speed - decelerationSpeed}")

    # abstraction
    @abstractmethod
    def description(self) -> str:
        pass

class Car(Vehicle): #inheritance
    def description(self) -> str:
        return f"The car is running with a speed of {self._speed}, and has a fuel capacity of {self._fuelCapacity}"

    # polymorphism
    def accelerate(self, accelerationSpeed: float) -> None:
        print(f"The car is running at a speed of {self._speed} and accelerates at {self._speed + accelerationSpeed}")
        self._speed += accelerationSpeed

    def decelerate(self, decelerationSpeed: float) -> None:
        print(f"The car is running at a speed of {self._speed} and decelerates at {self._speed - decelerationSpeed}")
        self.setSpeed(self._speed - decelerationSpeed)

class Truck(Vehicle): #inheritance
    def description(self) -> str:
        return f"The truck is running with a speed of {self._speed} and has a fuel capacity of {self._fuelCapacity}"

    # polymorphism
    def accelerate(self, accelerationSpeed: float = 5.0 if None else 5.0) -> None:
        print(f"The truck is running at a speed of {self._speed}, and accelerates at {self.speed + accelerationSpeed}")
        self._speed += accelerationSpeed

    def decelerate(self, decelerationSpeed: float) -> None:
        print(f"The truck is running at a speed of {self._speed} and decelerates at {self._speed - decelerationSpeed}")
        self.setSpeed(self._speed - decelerationSpeed)

if __name__ == "__main__":
    firstCar = Car(75.0, 15.0)
    firstTruck = Truck(60.0, 30.0)

    print("Testing description: ")
    print(firstCar.description())
    print(firstTruck.description() + "\nTesting acceleration/deceleration")

    firstCar.accelerate(10.0)
    firstTruck.decelerate(7.5)
    print("\nPrinting descriptions again to see the speeds")

    print(firstCar.description())
    print(firstTruck.description())

    exit(0)