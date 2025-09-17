
def simple_interest(principal, time, rate=10):
    si = (principal * rate * time) / 100
    return si


def compound_interest(principal, time, rate=10):
    amount = principal * ((1 + rate / 100) ** time)
    ci = amount - principal
    return ci


p = float(input("Enter Principal Amount: "))
t = float(input("Enter Time (in years): "))

si = simple_interest(p, t)
ci = compound_interest(p, t)

print(f"Simple Interest: {si:.2f}")
print(f"Compound Interest: {ci:.2f}")
print(f"Difference (CI - SI): {ci - si:.2f}")
