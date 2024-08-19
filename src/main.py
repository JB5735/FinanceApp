# Building a Compound Interest Calculator

# Principle amount
p = 0
# Interest Rate
r = 0
# Time (years)
t = 0
# Number (number compounded)
n = 0


while p <= 0:
    p = float(input("Enter the principle amount: "))
    if p < 0:
        print("Principle can't be less than 0")
    else:
        break

while n <= 0:
    n = float(input("Enter the number of times compounded per year: "))
    if n < 0:
        print("Number of times can't be less than 0")
    else:
        break

while r <= 0:
    r = 1 + ((float(input("Enter the interest rate: ")) / 100)/n)
    if r < 0:
        print("Interest rate can't be less than 0")
    else:
        break

while t <= 0:
    t = int(input("Enter the amount of time: "))
    if t < 0:
        print("Time can't be less than 0")
    else:
        break


total = "%.2f" % (p * (r**(n*t)))
print(f"Balance after {t} year(s): ${total}")
