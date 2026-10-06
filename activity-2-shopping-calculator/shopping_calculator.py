def calculate_total(price, tax_rate=0.20, discount=0,tip=0.12):
    subtotal = price - discount + price * tip
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total 


# Test cases
print(f"£{calculate_total(100):.2f}")
print(f"£{calculate_total(100, 0.1):.2f}")
print(f"£{calculate_total(100, 0.08, 10):.2f}")
print(f"£{calculate_total(100, 0.08, 10, 0):.2f}")