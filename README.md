# Codecademy Project: Len's Slice

![""](https://github.com/sarahm44/lens-slice/blob/main/pizza.jpg)

## Overview
For this project, I imagine I work at Len’s Slice, a new pizza joint in the neighborhood. I use my knowledge of Python lists to organize some of my sales data.

The Python notebook containing the code is [here](https://github.com/sarahm44/lens-slice/blob/main/lens_slices.py).

## Tasks
### Make Some Pizzas
1. To keep track of the kinds of pizzas you sell, create a list called <code>toppings</code> that holds the following:

* <code>"pepperoni"</code>
* <code>"pineapple"</code>
* <code>"cheese"</code>
* <code>"sausage"</code>
* <code>"olives"</code>
* <code>"anchovies"</code>
* <code>"mushrooms"</code>

![""](https://github.com/sarahm44/lens-slice/blob/main/task_01.png)

2. To keep track of how much each kind of pizza slice costs, create a list called <code>prices</code> that holds the following integer values:

* <code>2</code>
* <code>6</code>
* <code>1</code>
* <code>3</code>
* <code>2</code>
* <code>7</code>
* <code>2</code>

![""](https://github.com/sarahm44/lens-slice/blob/main/task_02.png)

3. Your boss wants you to do some research on $2 slices. Count the number of occurrences of <code>2</code> in the <code>prices</code> list, and store the result in a variable called <code>num_two_dollar_slices</code>. Print it out.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_03.png)

The code output is as follows:

![""](https://github.com/sarahm44/lens-slice/blob/main/output_03.png)


4. Find the length of the toppings list and store it in a variable called <code>num_pizzas</code>.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_04.png)

5. Print the string <code>We sell [num_pizzas] different kinds of pizza!</code>, where <code>[num_pizzas]</code> represents the value of our variable <code>num_pizzas</code>.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_05.png)

The code output is as follows:

![""](https://github.com/sarahm44/lens-slice/blob/main/output_05.png)

6. Use the existing data about the pizza toppings and prices to create a new two-dimensional list called <code>pizza_and_prices</code>.

Each sublist in <code>pizza_and_prices</code> should have one pizza topping and an associated price.

| Price |	Topping |
|----|----|
| <code>2</code> | <code>"pepperoni"</code> |
| <code>6</code> | <code>"pineapple"</code> |
| <code>1</code> | <code>"cheese"</code> |
| <code>3</code> | <code>"sausage"</code> |
| <code>2</code> | <code>"olives"</code> |
| <code>7</code> | <code>"anchovies"</code> |
| <code>2</code> | <code>"mushrooms"</code> |

For this new list make sure the prices come before the topping name like so:

<code>[price, topping_name]</code>

<b>Note:</b> You don’t need to use your original <code>toppings</code> and <code>prices</code> lists in this exercise. Create a new two-dimensional list from scratch.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_06.png)

7. Print <code>pizza_and_prices</code>.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_07.png)

The code output is as follows:

![""](https://github.com/sarahm44/lens-slice/blob/main/output_07.png)

### Sorting and Slicing Pizzas
8. Sort <code>pizza_and_prices</code> so that the pizzas are in the order of increasing price (ascending).

![""](https://github.com/sarahm44/lens-slice/blob/main/task_08.png)

The code output is as follows:

![""](https://github.com/sarahm44/lens-slice/blob/main/output_08.png)


9. Store the first element of <code>pizza_and_prices</code> in a variable called  <code>cheapest_pizza</code>.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_09.png)

The code output is as follows:

![""](https://github.com/sarahm44/lens-slice/blob/main/output_09.png)


10. A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”

Get the last item of the  <code>pizza_and_prices</code> list and store it in a variable called  <code>priciest_pizza</code>.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_10.png)

The code output is as follows:

![""](https://github.com/sarahm44/lens-slice/blob/main/output_10.png)


11. It looks like the most expensive pizza from the previous step was our very last  <code>"anchovies"</code> slice. Remove it from our  <code>pizza_and_prices</code> list since the man bought the last slice.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_11.png)

12. Since there is no longer an  <code>"anchovies"</code> pizza, you want to add a new topping called <code>"peppers"</code> to keep your customers excited about new toppings. Here is what your new topping looks like:

 <code>[2.5, "peppers"]</code>

Add the new peppers pizza topping to our list  <code>pizza_and_prices</code>.

<b>Note:</b> Make sure to position it relative to the rest of the sorted data in  <code>pizza_and_prices</code>, otherwise our data will not be correctly sorted anymore!

![""](https://github.com/sarahm44/lens-slice/blob/main/task_12.png)

13. Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

Slice the  <code>pizza_and_prices</code> list and store the 3 lowest cost pizzas in a list called  <code>three_cheapest</code>.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_13.png)

14. Great job! The mice are very pleased and will be leaving you a 5-star review.

Print the  <code>three_cheapest</code> list.

![""](https://github.com/sarahm44/lens-slice/blob/main/task_14.png)

The code output is as follows:

![""](https://github.com/sarahm44/lens-slice/blob/main/output_14.png)


