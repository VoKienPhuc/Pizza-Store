from Pizzas.Pizza import Pizza

class HaNoiCheesePizza(Pizza):
    
    _name = 'Hà Nội Cheese'
    _dough = 'thin'
    _sauce = 'super spicy'
    _topping = ['black olives', 'chicken']
    
    def bake(self):
        print(' Baking ' + self._name + ' pizza in 30 minutes')
     

class HaNoiGreekPizza(Pizza):
    
    _name = 'Hà Nội Greek'
    _dough = 'very thin'
    _sauce = 'tomato'
    _topping = ['chilli', 'shrimp']
    
    def cut(self):
        print(' Cutting ' + self._name + ' into 4 slices')
     

class HaNoiPepperoniPizza(Pizza):
    
    _name = 'Hà Nội Pepperoni'
    _dough = 'medium'
    _sauce = 'sweet'
    _topping = ['tomato', 'squid']
    