# Building a Tip Calculator

def tip_calc(cost, tip_percent):
    tip = float("%.2f" % (cost * (tip_percent / 100)))
    return tip


# Building a Tax Calculator

def tax_calc(cost, tax_percent):
    tax = float("%.2f" % ((cost * tax_percent) / 100))
    return tax


# Total Meal Cost Calculator

def meal_cost(cost, tip_percent, tax_percent):
    tip = tip_calc(cost, tip_percent)
    tax = tax_calc(cost, tax_percent)
    total = cost + tip + tax
    return total


cost = float(input("How much was the flat cost of the meal? "))
tip_percent = float(input("What percent would you like to tip? "))
tax_percent = float(input("What percent is being taxed? "))

total = meal_cost(cost, tip_percent, tax_percent)
print(f"Your total cost for the meal with a {tip_percent} tip and {tax_percent} tax is ${total}")