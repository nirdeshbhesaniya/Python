with open("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("Python is mentioned in the log file.")
else:
    print("Python is not mentioned in the log file.")