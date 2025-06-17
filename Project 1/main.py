import random
'''
1 for snake
-1 for water 
0 for gun
'''


computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You Chose: {reverseDict[you]}")
print(f"Computer Chose: {reverseDict[computer]}")

if you == computer:
    print("It's a Tie!")
else:
        if(computer ==-1 and you == 1): 
            print("You win!")

        elif(computer ==-1 and you == 0):
            print("You Lose!")

        elif(computer == 1 and you == -1):
            print("You lose!")

        elif(computer ==1 and you == 0):
            print("You Win!")

        elif(computer ==0 and you == -1):
            print("You Win!")

        elif(computer == 0 and you == 1):
            print("You Lose!")

        else:
            print("Something went wrong!")