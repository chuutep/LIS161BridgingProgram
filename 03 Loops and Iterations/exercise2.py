sum = 0
count = 0
min = None
max = None

while True:
    num = input("Enter number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print("Invalid input")
        continue

    sum += num
    count += 1

    if min is None or min > num:
        min = num
    if max is None or max < num:
        max = num

print(sum, count, sum/count, min, max)
