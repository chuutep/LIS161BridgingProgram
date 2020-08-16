def computegrade(s):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    elif score < 0.6:
        return "F"

score = input("Enter score: ")

try:
    score = float(score)
except:
    print("Bad score")
    exit()

if score > 1 or score < 0:
    print("Bad score")
    exit()

print(computegrade(score))
