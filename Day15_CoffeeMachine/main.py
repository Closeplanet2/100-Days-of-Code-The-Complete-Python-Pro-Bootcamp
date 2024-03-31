from Scripts.CoffeeMachine import CoffeeMachine

coffieMachine = CoffeeMachine(water=300, milk=200, coffee=100, price=0)
coffieMachine.add_stored_recipe("Espresso", water=50, coffee=18, milk=0, price=1.50)
coffieMachine.add_stored_recipe("Latte", water=200, coffee=24, milk=150, price=2.50)
coffieMachine.add_stored_recipe("Cappuccino", water=250, coffee=24, milk=100, price=3.00)
coffieMachine.game_loop()