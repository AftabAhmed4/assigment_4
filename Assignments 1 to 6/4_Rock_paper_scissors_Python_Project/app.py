import random

def play():
    user = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    
    # Check win conditions for user
    if is_win(user, computer):
        return "You win! 🎉"
    
    return "You lost! 😢"

def is_win(player, opponent):
    # Return True if player beats opponent
    return (
        (player == "rock" and opponent == "scissors") or
        (player == "scissors" and opponent == "paper") or
        (player == "paper" and opponent == "rock")
    )

# Run the game
print(play())
