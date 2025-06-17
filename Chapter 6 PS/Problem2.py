mark1 = int(input("Enter Subject1 marks:"))
mark2 = int(input("Enter Subject2 marks:"))
mark3 = int(input("Enter Subject3 marks:"))

total_parsentage = (100*(mark1+mark2+mark3))/300

if(total_parsentage >= 40 and mark1>33 and mark2>33 and mark3>33):
    print("You are pass in exam",total_parsentage)
else:
     print("You failed, try again next year:", total_parsentage)
