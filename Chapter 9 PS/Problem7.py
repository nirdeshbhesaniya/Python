with open("log.txt") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes python is mentioned in the log file at line {lineno}.")
        break
    lineno += 1
else:
    print("No python is not mentioned in the log file.")