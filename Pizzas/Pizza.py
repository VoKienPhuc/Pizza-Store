""" Scripts for Pizza"""

from abc import ABC


class Pizza(ABC):
    
    _name = ''
    _dough = ''
    _sauce = ''
    _topping = []
    
    def prepare(self):
        
        print(" Prepare for making a " + self._name + " pizza")
        print(" Tossing " + self._dough + " dough ...")
        print(" Adding " + self._sauce + " sauce ...")
        for topping in self._topping:
            print(" Adding " + topping + " topping")
    
    def bake(self):
        print(" Baking " + self._name + " pizza in 20 minutes")
    
    def cut(self):
        print(" Cutting " + self._name + " into 8 slices")
    
    def box(self):
        print(" Boxing the " + self._name + " pizza")
 