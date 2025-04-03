#Assignment 1

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return round(final_price, 2)
    return price

test_price = 100
test_discount = 25

result = calculate_discount(test_price, test_discount)
print(f"Original price: ${test_price}")
print(f"Discount: {test_discount}%")
print(f"Final price: ${result}")




#Assignment 2
    
def calculate_discount_interactive():
    try:
        price = float(input("Enter the original price: $"))
        discount = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(price, discount)
        
        if discount >= 20:
            print(f"\nOriginal price: ${price}")
            print(f"Discount applied: {discount}%")
            print(f"Final price: ${final_price}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Final price: ${final_price}")
            
    except ValueError:
        print("Error: Please enter valid numbers for price and discount")


calculate_discount_interactive()
