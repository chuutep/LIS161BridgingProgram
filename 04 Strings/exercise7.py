str ="X-DSPAM-Confidence:0.8475"

dspam = float(str[str.find(':') + 1:])
print(dspam)
