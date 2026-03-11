def calculate_due(Total,amount_paid):
    return Total - amount_paid
bill= float(input("enter a total bill amount"))
paid= float(input("enter asmont paid"))
due= calculate_due(bill,paid)
print("customer due amout is",calculate_due)