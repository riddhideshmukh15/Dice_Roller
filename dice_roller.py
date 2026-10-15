
import random

while True:
    print("\n===== DICE ROLLER =====")
    print("1. Roll the dice")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            dice = random.randint(1, 6)
            print(f"You rolled: {dice}")

            again = input("Do you want to roll again? (yes/no): ").lower()

            if again == "yes":
                continue
            elif again == "no":
                break
            else:
                print("Invalid choice! Please enter yes or no.")

    elif choice == "2":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice! Please try again.")
