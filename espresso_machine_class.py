# Description: The EspressoMachine class returns the name of the drink with the number of espresso shots and the water tank and coffee capacity after making that drink. 

class EspressoMachine:
    # class variables.
    canMakeEspresso = True
    menu_list = ['Cappuccino', 'Latte', 'Mocha']
    def __init__(self, drink, num_of_espresso_shots, water_tank_capacity, coffee_capacity):
        # data variables.
        self._drink = drink
        self._num_of_espresso_shots = num_of_espresso_shots
        self._water_tank_capacity = water_tank_capacity
        self._coffee_capacity = coffee_capacity

    def can_it_make_espresso(self):
        return self.canMakeEspresso

    # Gets current water capacity.
    def get_water_capacity(self):
        # Returns error message if water_tank_capacity = 0.
        if self._water_tank_capacity == 0:
            return ("No more water!")
        else: 
            return self._water_tank_capacity

    # Gets current coffee capcity.
    def get_coffee_capacity(self):
        # Returns error message if coffee_capacity = 0.
        if self._coffee_capacity == 0:
            return ("No more coffee!")
        else: 
            return self._coffee_capacity

    # Returns string message and water tank and coffee capacity after making one espresso shot. 
    def make_single_shot(self):
        # Subtracts from water and coffee capacity when fucntion is called.
        self._water_tank_capacity = self._water_tank_capacity - 1
        self._coffee_capacity = self._coffee_capacity - 2
        # returns string message with current capacities.
        return (f'Single shot!\nWater Capacity: {self.get_water_capacity()}\nCoffee Capacity: {self.get_coffee_capacity()}')
   
    # Method for making drink.
    def make_drink(self):
        # Loops through menu_list (list of strings). 
        for i in self.menu_list:
            # Checks if i is the same as drink in the argument.
            if (i == self._drink):
                # Loops a specific number of times based on number of espresso shots as inputted in the argument. 
                for a in range(1, self._num_of_espresso_shots+1):
                    # Checks to see if coffee or water capcity is 0 and prints error if empty.
                    if (self._coffee_capacity == 0) or (self._water_tank_capacity == 0):
                        return ("Can't complete order!")
                    # If coffee and water capacity not empty, calls make_single_shot() function.
                    else:
                        self.make_single_shot()
        # returns string of the drink made, how many espresso shots, and the water and coffee capacity after making the drink.                
        return (f'Drink made!\n{self._drink} with {a} espresso shots.\nWater Capacity: {self.get_water_capacity()}\nCoffee Capacity: {self.get_coffee_capacity()}')

def main():
    # In order to "make" a drink, the following arguments need to be entered.
    # EspressoMachine("name of drink", number of espresso shots, water tank capacity, coffee capacity)
    # For the first argument, there are only 3 possible options: "Latte", "Cappuccino", "Mocha". (need to be entered as a string)

    L = EspressoMachine('Latte', 4, 5, 10)
    print(L.make_drink())
    print(f'Makes espresso: {L.can_it_make_espresso()}')

    C = EspressoMachine('Cappuccino', 2, 3, 12)
    print(C.make_drink())
    print(f'Makes espresso: {C.can_it_make_espresso()}')


    M = EspressoMachine('Mocha', 3, 3, 6)
    print(M.make_drink())
    print(f'Makes espresso: {M.can_it_make_espresso()}')


if __name__ == "__main__":
    main()