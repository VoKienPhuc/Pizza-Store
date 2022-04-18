from Stores.PizzaStore import HoChiMinhStore, DaNangStore, HaNoiStore

hcm_store = HoChiMinhStore()
hcm_store.order_pizza('pepperoni')

danang_store = DaNangStore()
danang_store.order_pizza('cheese')

hanoi_store = HaNoiStore()
hanoi_store.order_pizza('burger')