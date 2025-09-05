def random_quote():
    """
    Returns a random motivational or fun quote.
    Author: Ayush Pareek
    """
    quotes = [
        "Keep going, you’re doing great!",
        "Bug-free code is a myth, but we try anyway!",
        "Coffee + Code = Happiness",
        "Every expert was once a beginner.",
        "Push early, push often!"
    ]
    return random.choice(quotes)

# ----------------------------
# Admin Driver
# ----------------------------

def main():
    print("🎮 Mini Games Menu 🎮")
    print("1. Roll Dice")
    print("2. Coin Toss")
    print("3. Guess Number")
    print("4. Rock-Paper-Scissors")
    print("5. Random Quote")
    choice = input("Choose a game (1-5): ")

    if choice == "1":
        print("Dice rolled:", roll_dice())

    elif choice == "2":
        print("Coin toss result:", coin_toss())

    elif choice == "3":
        secret = random.randint(1, 10)
        guess_val = int(input("Enter your guess (1-10): "))
        print(guess_number(secret, guess_val))

    elif choice == "4":
        player = input("Enter rock, paper, or scissors: ").lower()
        computer = random.choice(["rock", "paper", "scissors"])
        print("Computer chose:", computer)
        print(rps(player, computer))

    elif choice == "5":
        print("Quote of the day:", random_quote())

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
