hours = input("Enter hour: ")
rate = input("Enter rate: ")

try:
    hours = float(hours)
except:
    print("Value error for hours")
    exit()
try:
    rate = float(rate)
except:
    print("Value error for rate")
    exit()

if hours > 40:
    pay = 40 * rate + (hours-40)*rate*1.5
else:
    pay = hours * rate

print("Pay: ", pay)
