import random

def play_game():
    """The main logic for the Number Guessing Game."""
    
    print("\n" + "="*30)
    print("  WELCOME TO THE GUESSER  ")
    print("="*30)
    
    # Generate a secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("I have chosen a number between 1 and 100.")
    print("Can you find it, Subhan Yasir?")
    
    # The Game Loop
    while not guessed_correctly:
        user_input = input("\nEnter your guess (or type 'quit'): ").lower()
        
        # 1. Check if user wants to exit
        if user_input == 'quit':
            print(f"The secret number was {secret_number}. Goodbye!")
            break
            
        # 2. Try-Except to handle non-number inputs (Professional Style)
        try:
            guess = int(user_input)
            attempts += 1  # Count this guess
            
            # 3. The Comparison Logic
            if guess > secret_number:
                print("--- Lower number please ---")
            elif guess < secret_number:
                print("--- Higher number please ---")
            else:
                # Success!
                print("\n" + "*"*30)
                print(f"CONGRATULATIONS, SUBHAN!")
                print(f"You found the number {secret_number}!")
                print(f"It took you {attempts} attempts.")
                print("*"*30)
                guessed_correctly = True
                
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def show_menu():
    """Displays the starting menu for the user."""
    while True:
        print("\n--- Game Menu ---")
        print("1. Start New Game")
        print("2. View Game Rules")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            play_game()
        elif choice == '2':
            print("\nRULES:")
            print("- Guess a number between 1 and 100.")
            print("- I will tell you to go Higher or Lower.")
            print("- Try to win in the fewest guesses possible!")
        elif choice == '3':
            print("Thanks for playing, Subhan Yasir. See you next time!")
            break
        else:
            print("Please select a valid option (1, 2, or 3).")

# This starts the whole program
if __name__ == "__main__":
    show_menu()