# To create an abstract class - extend it with ABC and use @abstractmethod decorator
# To define an abstract method we use the @abstractmethod decorator of the abc module. Such method should be overridden in the child classes otherwise Error will be thrown


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def run(self):
        pass

    def openGate(self):
        print("Abstract Gate Opened")

class Car(Vehicle):

    def run(self):
        print("Car running")

# If run hasn't been defined, the code would have thrown an error
v = Car()
v.openGate()
v.run()
