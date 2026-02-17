import vending_machine as vm

class RefrigeratedVendingMachine(vm.VendingMachine):
    """
    A specialized Vending Machine that keeps drinks cold.
    """
    def __init__(self, item_name, item_price, stock, target_temp):
        # 1. Use super() to call the parent's __init__ 
        # This handles name, price, and stock so we don't have to!
        super().__init__(item_name, item_price, stock)
        
        # 2. Add a new attribute unique to this subclass
        self.target_temp = target_temp 
        self.current_temp = target_temp + 5.0 # Starts a bit warm

    def cool_down(self):
        """A new method specific to refrigerated machines."""
        self.current_temp = self.target_temp
        print(f"Cooling system activated. Current temp: {self.current_temp}°C")

    def purchase(self):
        """
        Calls parent class purchase method but is this ok? Is the product temperature cool enough to sell the product?
        """
        if self.current_temp > self.target_temp:
            print(f"Sorry, {self.item_name} is too warm to sell! Current temp: {self.current_temp}°C")
        else:
            super().purchase()

