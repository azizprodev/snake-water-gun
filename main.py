import random

def get_user_choice():
    choices = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
    print("\nEnter your choice:\n's' for Snake\n'w' for Water\n'g' for Gun")
    user_input = input("Your choice: ").lower()
    while user_input not in choices:
        print("Invalid choice. Please enter 's', 'w', or 'g'.")
        user_input = input("Your choice: ").lower()
    return user_input, choices[user_input]

def get_computer_choice():
    choices = ['s', 'w', 'g']
    computer_choice = random.choice(choices)
    return computer_choice, {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}[computer_choice]

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 's' and computer == 'w') or (user == 'w' and computer == 'g') or (user == 'g' and computer == 's'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Snake Water Gun Game!")
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice, user_choice_full = get_user_choice()
        computer_choice, computer_choice_full = get_computer_choice()
        
        print(f"\nYou chose: {user_choice_full}")
        print(f"Computer chose: {computer_choice_full}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"Scores -> You: {user_score}, Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\nThanks for playing! Final Scores -> You: {}, Computer: {}".format(user_score, computer_score))

if __name__ == "__main__":
    main()
