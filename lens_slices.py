# Create a list called "toppings"
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Create a list called "prices"
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of occurences of 2 in "prices"
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Find length of the "toppings" list
num_pizzas = len(toppings)

# Print in a string
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Create two dimensional list with pizza and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Print pizza and prices list
print(pizza_and_prices)

# Sort pizzas an prices, with price small to high (ascending)
pizza_and_prices.sort()
print(pizza_and_prices)

# Create variable cheapest_pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# Create variable priciest_pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Remove anchovies
pizza_and_prices.pop()

# Add peppers
pizza_and_prices.insert(4, [2.5, "peppers"])

# Find three cheapest pizzas
three_cheapest = pizza_and_prices[0:3]

# Print the three cheapest
print(three_cheapest)
