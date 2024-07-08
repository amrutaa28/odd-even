import random

# Function for Number Guessing Game
def number_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try guessing higher.")
            elif guess > secret_number:
                print("Too high! Try guessing lower.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                return

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nSorry, you ran out of attempts. The number was {secret_number}.")

# Function for Dice Rolling Game
def dice_rolling_game():
    print("\nWelcome to the Dice Rolling Game!")

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print(f"You rolled {dice1} and {dice2}. Total: {total}")

    if total % 2 == 0:
        print("Congratulations! It's an even number. You win!")
    else:
        print("Oops! It's an odd number. You lose.")

# Function for Word Guessing Game
def word_guessing_game():
    print("\nWelcome to the Word Guessing Game!")
    words = ["apple", "banana", "cherry", "orange", "grape"]
    secret_word = random.choice(words)
    max_attempts = 5
    guesses = []

    while max_attempts > 0:
        guess = input("\nEnter a letter or guess the word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guesses:
                print(f"You already guessed '{guess}'. Try another letter.")
            elif guess in secret_word:
                print(f"Correct! '{guess}' is in the word.")
                guesses.append(guess)
                if all(letter in guesses for letter in secret_word):
                    print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
                    return
            else:
                print(f"'{guess}' is not in the word. Try again.")
                guesses.append(guess)
                max_attempts -= 1
                print(f"You have {max_attempts} attempts left.")
        elif guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
            return
        else:
            print("Invalid input. Please enter a single letter or guess the whole word.")

    print(f"\nSorry, you ran out of attempts. The word was '{secret_word}'.")

# Main game function
def main():
    print("Welcome to the Three-in-One Game!")

    while True:
        print("\nChoose a game to play:")
        print("1. Number Guessing Game")
        print("2. Dice Rolling Game")
        print("3. Word Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            dice_rolling_game()
        elif choice == '3':
            word_guessing_game()
        elif choice == '4':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

