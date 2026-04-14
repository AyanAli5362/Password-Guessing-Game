import random

easy_words = ["fruits", "train", "tiger", "name", "tree", "bat", "doctor", "bus"]
medium_words = ["secret", "repeat", "regular", "creature", "familiar", "interest", "human"]
hard_words = ["think", "supposed", "ai", "rhythm", "yatch", "unknown"]
  
print("\nWelcome to Password-Guessing-Game")
print("Choose the Level of Game: Easy, Medium or Hard")

level = input('Enter the level of Difficulty: ').lower()

if level == 'easy':
    secret = random.choice(easy_words)

elif level == 'medium':
    secret = random.choice(medium_words)

elif level == 'hard':
    secret = random.choice(hard_words)

else:
    print('Invalid Choice, Please Choose Correct Choice -> Difficult to Easy level  ')
    secret = random.choice(easy_words) # call easy level to default


Attempts = 0
print("\nGuess the Secret Password")

while True:
    guess = input("Enter your guess: ").lower()
    Attempts += 1

    if guess == secret:
        print(f"Congratulations: To Guessing the Correct Password in {Attempts} Attempts.")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]

        else:
            hint += "_"

    print("Hint: ", hint)

print("Game Over")