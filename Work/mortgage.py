# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = int(input('Extra Payment Start Month?'))
extra_payment_end_month = int(input('Extra Payment End Month?'))
extra_payment = int(input('Extra Payment Amount Per Month?')) # per month
months_total = 0

while principal > 0:
    while months_total >= extra_payment_start_month and months_total <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        #principal = principal - extra_payment
        total_paid = total_paid + payment + extra_payment
        months_total += 1
        print((months_total-1), total_paid, principal)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months_total += 1
    if principal < 0:
        principal -= principal
    print((months_total-1), total_paid, principal)

print('Total paid', total_paid)
print('Total Number of Months', months_total)

