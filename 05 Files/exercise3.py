filename = input("Enter filename: ")

if filename == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    exit()

try:
    fhandle = open(filename)
except:
    print("File not found!")
    exit()

subject_lines = 0
for line in fhandle:
    if line.startswith('subject'):
        subject_lines += 1

print("There were {sub} subject lines in {file}".format(sub=subject_lines,file=filename))
