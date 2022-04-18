from Pizzas.Pizza import Pizza

class DaNangCheesePizza(Pizza):
    
    _name = 'Đà Nẵng Cheese'
    _dough = 'thin'
    _sauce = 'super spicy'
    _topping = ['black olives', 'chicken']
    
    def bake(self):
        print(' Baking ' + self._name + ' pizza in 30 minutes')
     

class DaNangGreekPizza(Pizza):
    
    _name = 'Đà Nẵng Greek'
    _dough = 'very thin'
    _sauce = 'tomato'
    _topping = ['chilli', 'shrimp']
    
    def cut(self):
        print(' Cutting ' + self._name + ' into 4 slices')
     

class DaNangPepperoniPizza(Pizza):
    
    _name = 'Đà Nẵng Pepperoni'
    _dough = 'medium'
    _sauce = 'sweet'
    _topping = ['tomato', 'squid']
    