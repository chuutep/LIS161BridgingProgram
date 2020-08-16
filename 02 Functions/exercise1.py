def computepay(h,r):
    if h > 40:
        pay = 40*r+(h-40)*r*1.5
    else:
        pay = h*r
    return pay

h = input("Enter hour: ")

try:
    h = float(h)
except:
    print("Value error for hours")
    exit()

r = input("Enter rate: ")

try:
    r = float(r)
except:
    print("Value error for rate")
    exit()

print("Pay: ", computepay(h,r))
