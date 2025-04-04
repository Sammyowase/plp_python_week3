# Discount Calculator

This program implements a discount calculator that applies discounts to prices based on a percentage threshold.

## Features

- Calculates discounts for prices with a minimum threshold of 20%
- Provides both automated test cases and interactive input
- Handles invalid inputs gracefully
- Rounds final prices to 2 decimal places

## Usage

The program contains two main functions:

1. `calculate_discount(price, discount_percent)`: Core function that calculates the discounted price
   - Takes a price and discount percentage as parameters
   - Returns the original price if discount is less than 20%
   - Returns discounted price if discount is 20% or higher

2. `calculate_discount_interactive()`: Interactive version that prompts for user input
   - Asks for the original price
   - Asks for the discount percentage
   - Displays the results with appropriate messaging

## Example Output

```
Enter the original price: $100
Enter the discount percentage: 25

Original price: $100
Discount applied: 25%
Final price: $75.00
```

## Error Handling

The program includes error handling for:
- Invalid numeric inputs
- Non-numeric inputs
- Proper formatting of currency values
