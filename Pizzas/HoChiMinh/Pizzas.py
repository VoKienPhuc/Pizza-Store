from Pizzas.Pizza import Pizza

class HoChiMinhCheesePizza(Pizza):
    
    _name = 'TP HCM Cheese'
    _dough = 'thin'
    _sauce = 'super spicy'
    _topping = ['black olives', 'chicken']
    
    def bake(self):
        print(' Baking ' + self._name + ' pizza in 30 minutes')
     

class HoChiMinhGreekPizza(Pizza):
    
    _name = 'TP HCM Greek'
    _dough = 'very thin'
    _sauce = 'tomato'
    _topping = ['chilli', 'shrimp']
    
    def cut(self):
        print(' Cutting ' + self._name + ' into 4 slices')
     

class HoChiMinhPepperoniPizza(Pizza):
    
    _name = 'TP HCM Pepperoni'
    _dough = 'medium'
    _sauce = 'sweet'
    _topping = ['tomato', 'squid']
    