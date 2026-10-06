# Three of the things below are wrong. The code runs without crashing,
# which is exactly what makes them worth finding.


def calculate_area(length, width):
    # area = length * width
    # this function did not return anything
    # I fixed it by adding a return statement
    area = length * width
    return area


def apply_discount(price, discount_percent):
    reduction = price * discount_percent / 100
    # return price - discount_percent
    new_price = price - reduction
    return new_price


def convert_to_percentage(part, whole):
    return (part / whole) * 100
# when the function is called, it should insert the parameters values the other way around


print(calculate_area(4, 5))
print(apply_discount(80, 25))
# print(convert_to_percentage(200, 50))
print(convert_to_percentage(50, 200))
