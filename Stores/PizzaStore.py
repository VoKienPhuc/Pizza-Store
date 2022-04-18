""" Scripts for Pizza Store"""

from abc import ABC, abstractmethod

from Pizzas.HaNoi.Pizzas import HaNoiCheesePizza, HaNoiGreekPizza, HaNoiPepperoniPizza
from Pizzas.DaNang.Pizzas import DaNangCheesePizza, DaNangGreekPizza, DaNangPepperoniPizza
from Pizzas.HoChiMinh.Pizzas import HoChiMinhCheesePizza, HoChiMinhGreekPizza, HoChiMinhPepperoniPizza


class PizzaStore(ABC):
    
    def order_pizza(self, type):
        
        my_pizza = self.define_pizza(type)
        if my_pizza == None:
            print(" We do not have {} pizza here".format(type))
            return
        
        my_pizza.prepare()
        my_pizza.bake()
        my_pizza.cut()
        my_pizza.box()
        
    @abstractmethod
    def define_pizza(self, type):
        pass


class HoChiMinhStore(PizzaStore):
    
    def define_pizza(self, type):
        
        if type == 'cheese':
            return HoChiMinhCheesePizza()
        elif type == 'greek':
            return HoChiMinhGreekPizza()
        elif type == 'pepperoni':
            return HoChiMinhPepperoniPizza()
        else:
            return None


class HaNoiStore(PizzaStore):
    
    def define_pizza(self, type):
        if type == 'cheese':
            return HaNoiCheesePizza()
        elif type == 'greek':
            return HaNoiGreekPizza()
        elif type == 'pepperoni':
            return HaNoiPepperoniPizza()
        else:
            return None


class DaNangStore(PizzaStore):
    
    def define_pizza(self, type):
        if type == 'cheese':
            return DaNangCheesePizza()
        elif type == 'greek':
            return DaNangGreekPizza()
        elif type == 'pepperoni':
            return DaNangPepperoniPizza()
        else:
            return None

