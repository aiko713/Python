# Make some pizzas:
toppings = ["pepperoni","pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#Number of 2 dollar slices
num_two_dollar_slices = prices.count(2)

#Number of pizzas
num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

# 2D list 
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

#Sorting and Slicing 
pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

pizza_and_prices.insert(4, [2.5,"peppers"])
print(pizza_and_prices)

# Three mice got the 3 lowest cost pizzas! 
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)