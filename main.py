def guess_number(secret, guess):
    """
    Compares guess with secret number and returns result string.
    Author: Gaikwad Aman Anand
    """
    if guess == secret:
        return "Correct!"
    elif guess < secret:
        return "Too low!"
    else:
        return "Too high!"

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
