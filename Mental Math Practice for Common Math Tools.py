import random
import sys

# Global status variable
Question_Progress = 0

def run_powers_test():
    global Question_Progress
    
    # We use a local loop here so we can stay in the "Powers" section
    while Question_Progress < 20:
        print(f"\n--- Question {Question_Progress + 1} of 20 ---")
        print("Difficulty: 1. Easy | 2. Medium | 3. Hard | 4. Quit")
        difficulty = input("Choice: ")

        if difficulty == "4":
            print("Exiting to Main Menu...")
            return # Returns to the main_menu() function

        # Set up difficulty parameters
        if difficulty == "1":
            base, exp = 2, random.randint(1, 10)
        elif difficulty == "2":
            base, exp = random.randint(3, 10), random.randint(1, 5)
        elif difficulty == "3":
            base, exp = random.randint(1, 20), random.randint(1, 10)
        else:
            print("Invalid choice.")
            continue

        answer = base ** exp
        user_input = input(f"What is {base}^{exp}? ")

        # Check if input is a number to prevent crashing
        if user_input.isdigit():
            if int(user_input) == answer:
                print("Correct!")
                Question_Progress += 1
            else:
                print(f"Wrong! The correct answer is {answer}.")
        else:
            print("Please enter a valid number.")

    print("\nPractice complete!")
    Question_Progress = 0 # Reset for next time

def main_menu():
    while True: # This keeps the whole program running
        print("\n=== Welcome to Math Practice! ===")
        print("1. Powers")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            run_powers_test()
        elif choice == "2":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice.")

# Start the program
if __name__ == "__main__":
    main_menu()