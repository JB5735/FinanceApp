# Building a Compound Interest Calculator

# Principle amount
p = 0
# Interest Rate
r = 0
# Time (years)
t = 0


while p <= 0:
    p = float(input("Enter the principle amount: "))
    if p <= 0:
        print("Principle can't be less than or equal to 0")

while r <= 0:
    r = 1 + (float(input("Enter the interest rate: ")) / 100)
    if r <= 0:
        print("Interest rate can't be less than or equal to 0")

while t <= 0:
    t = int(input("Enter the amount of time: "))
    if t <= 0:
        print("Time can't be less than or equal to 0")

total = "%.2f" % (p * (r**t))
print(f"Balance after {t} year(s): ${total}")
