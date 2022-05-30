"""
Create abstract class ‘Pizza’ with bake method as abstract,
so that other classes inherit this and have to override the bake method.
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def bake(self):
        pass


class CheesePizza(Pizza):
    def bake(self):
        print("Baking....")


CheesePizza().bake()
