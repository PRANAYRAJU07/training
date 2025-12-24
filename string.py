import random

# Word list
words = [
    "apple", "grape", "mango", "peach", "berry", "lemon",
    "melon", "cherry", "guava", "olive", "papaya", "plums",
    "apron", "beach", "brick", "cabin", "camel", "candy",
    "chair", "clock", "cloud", "crown", "dance", "dream",
    "drink", "eagle", "earth", "flame", "floor", "fruit",
    "ghost", "giant", "glove", "grass", "green", "happy",
    "heart", "house", "human", "juice", "knife", "light",
    "lucky", "magic", "money", "music", "night", "ocean",
    "plant", "queen", "quick", "river", "round", "royal",
    "scale", "smile", "snake", "sound", "spice", "spoon",
    "stone", "storm", "sugar", "table", "tiger", "touch",
    "train", "unity", "value", "water", "wheel", "white",
    "world", "youth", "zebra", "solid", "faith", "skill",
    "focus", "brain", "sharp", "logic", "codey", "array",
    "class", "input", "print", "while", "break", "float",
    "range", "stack", "queue", "graph", "nodes", "edges"
]


secret_word = random.choice(words)
attempts = 6

print("🎯 Welcome to Python Wordle!")
print("Guess the 5-letter word")
print("✅ Correct position | 👍 Wrong position | ❌ Not in word")
print("-" * 40)

for attempt in range(1, attempts + 1):
    guess = input(f"Attempt {attempt}/6: ").lower()

    if len(guess) != 5:
        print("❌ Enter exactly 5 letters")
        continue

    result = []

    for i in range(5):
        if guess[i] == secret_word[i]:
            result.append("✅")
        elif guess[i] in secret_word:
            result.append("👍")
        else:
            result.append("❌")

    print(" ".join(result))

    if guess == secret_word:
        print("Congratulations! You guessed the word!")
        break
else:
    print(f"Game Over! The word was: {secret_word}")
