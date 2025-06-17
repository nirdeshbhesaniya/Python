for i in range(100):
    if i == 50:
        print("Halfway there!")
        continue  # Skip the rest of the loop when i is 50
    if i == 90:
        print("Almost done!")
        break  # Exit the loop when i is 90
    print(i)