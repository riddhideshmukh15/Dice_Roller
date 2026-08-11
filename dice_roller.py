import random
while True:
    print("=====Dice Roller=====")
    print("1:Roll the dice")
    print("2:Exit")

    choice=input("enter your choice :")
    if choice=="1":
       dice= random.randint(1,6)
       print(f"you rolled :{dice} ")
    elif choice=="2":
        print("Thanks for Playing!")
        break
    else:
        print("Invalid choice!please try again. ")
  